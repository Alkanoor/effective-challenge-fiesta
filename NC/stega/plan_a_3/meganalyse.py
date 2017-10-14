import sys, os

from PIL import ImageTk, Image
import Tkinter
Tkinter.Tk()
if sys.version_info < (3, 0):
    import Tkinter as tk
    from tkFileDialog import askopenfilename, asksaveasfilename
else:
    import tkinter as tk
    from tkinter.filedialog import askopenfilename, asksaveasfilename


main_filepath = 'Asteriksme-plana3_bottom.bmp'
main_image = ""
original_image = ""
image_values = []
bands = []

def init_image_values():
    global image_values, bands, main_filepath
    image_values = []
    for i in bands:
        bandvalue = [i, False, False, tk.IntVar(), tk.IntVar()]
        bandvalue[-1].set(1)
        bandvalue[-1].set(-1)
        lsb = []
        for j in range(8):
            lsb.append(tk.IntVar())
            if j < 7:
                lsb[-1].set(0)
            else:
                lsb[-1].set(1)

        bandvalue.append(lsb)  # lsb for the 8 bits of the band
        bandvalue.append(1)  # mask
        image_values.append(bandvalue)
    """Gobal value :
    LSB_bit as a filter
    [Zoomlevel, Current x,y]
    [Text(startx:y),Text(stopx:y),starting_at=0,one_pixel_every=1,bit_per_pixel=8,verbose=2,sens_lecture=2,bits_arrangement=[7,6,5,4,3,2,1,0],min_char_length,alphabet]
    Sens de lecture (0= toutes les lignes jusquau stop. 1= dans le rectangle start/stop,2 en serpant sur Y(x de 0 a x puis de x a 0) , 3 idem en y)
    [nb rotation 90 droite, flip_horizontal,flip vertical]
    #Resizing the log frame [has_clicked_on_the_resize : Boolean, Y0="""
    global_values = []
    # lsb_bits_as_filter
    lsb_bits = tk.IntVar()
    lsb_bits.set(0)
    global_values.append(lsb_bits)
    # zoomlevel/image debut x,y / imagefin x,y
    zoom = [0, 0, 0, 0, 0]
    global_values.append(zoom)
    # Start/Stop xy and every lsb analyse caracteristics
    sens = tk.IntVar()
    sens.set(2)
    lsb_chars = [0, 0, 0, 0, 0, 0, sens, 0, 0, 0]
    global_values.append(lsb_chars)
    # lecture horizontale/verticale
    reading = tk.IntVar()  # int
    reading.set(0)
    global_values.append(reading)
    # Rotations et Flips (rotation = x * 90 a droite, flip horizontal,flip_vertical)
    sens = [0, 0, 0]
    global_values.append(sens)
    # Resizing the log frame [has_clicked_on_the_resize : Boolean, Y0= //global_values[5]
    resize_log = [False, 0]
    global_values.append(resize_log)
    image_values.append(global_values)

    image = Image.open(main_filepath)
    # current x/y
    image_values[-1][1][3] = image.size[0]
    image_values[-1][1][4] = image.size[1]


def lsb_meganalyse(filepath="", image="", values=[]):
    if filepath != "":
        image = Image.open(filepath)
        # Reset the orientation right
        # flip rightleft
        if values[-1][4][1] % 2 == 1:
            image, a = f_flip_image(image=image, rightleft=True)
        # flip up down
        if values[-1][4][2] % 2 == 1:
            image, a = f_flip_image(image=image, rightleft=False)
        # Rotation
        for i in range(values[-1][4][0] % 4):
            image, a = f_rotate_image(image=image, right=True)
    raw_data = []
    data = ""
    fromx = 0
    fromy = 0
    tox = int(values[-1][2][1].get(1.0, tk.END).split(":")[0])
    toy = int(values[-1][2][1].get(1.0, tk.END).split(":")[1])

    # variables
    # lsb_chars : [Text(startx:y),Text(stopx:y),starting_at=0,one_pixel_every=1,bit_per_pixel=8,verbose=2,sens_lecture=2,bits_arrangement=[7,6,5,4,3,2,1,0]]
    starting_at = int(values[-1][2][2].get(1.0, tk.END))
    one_pixel_every = int(values[-1][2][3].get(1.0, tk.END))
    lsb_bit = values[0][6]  # NOT ENOUGH
    bit_per_pixel = int(values[-1][2][4].get(1.0, tk.END))
    verbose = int(values[-1][2][5].get(1.0, tk.END))
    sens_lecture = int(values[-1][2][6].get())
    bits_arrangement = values[-1][2][7].get(1.0, tk.END).split(",")
    for index, i in enumerate(bits_arrangement): bits_arrangement[index] = int(
        i)
    min_char_length = int(values[-1][2][8].get(1.0, tk.END))
    alphabet = values[-1][2][9].get()
    print(
        "Running LSB extraction from %i:%i to %i:%i" % (
            fromx, fromy, tox, toy))
    print(
        "Extracting one pixel every %i pixels, with an offset of %i,doing it in %i direction(s) " % (
            one_pixel_every, starting_at, sens_lecture))
    print("Lookinf for %i consecutive chars from alphabet %s" % (
        min_char_length, alphabet))
    if values[-1][3].get() == 1:
        print("Reading in a quand from start to stop")
    elif values[-1][3].get() == 0:
        print("Reading every pixels between start to stop")

    """now we can start gathering bits"""
    pix_data = image.load()
    Rawtab = []
    myrgb = []
    for i in range(len(values[:-1])):  # For each band
        Rawtab.append([])
        myrgb.append([i, values[i][0]])
    count = 0
    for y in range(fromy, toy + 1):
        if values[-1][3].get() == 1:  # Reading in a quand from start to stop
            for x in xrange(fromx, tox + 1):
                if (count) % one_pixel_every == 0:
                    if isinstance(pix_data[x, y], int):
                        value = [pix_data[x, y]]
                    else:
                        value = list(pix_data[x, y])
                    if verbose >= 2: print("x,y:", x, y, pix_data[x, y], value)
                    for index, band in enumerate(values[:-1]):
                        # Apply bit filtering
                        Rawtab[index].append(value[index] & band[6])
                count += 1
        elif values[-1][
            3].get() == 0:  # Reading every pixels between start to stop
            for x in xrange(image.size[0]):
                if y == fromy and x < fromx:
                    continue
                elif y == toy and x > tox:
                    break
                else:
                    if (count) % one_pixel_every == 0:
                        if isinstance(pix_data[x, y], int):
                            value = [pix_data[x, y]]
                        else:
                            value = list(pix_data[x, y])
                        if verbose >= 2: print(
                            "x,y:", x, y, pix_data[x, y], value)
                        for index, band in enumerate(values[:-1]):
                            # Apply bit filtering
                            Rawtab[index].append(value[index] & band[6])
                    count += 1
    if verbose >= 1: print("Extracted %i pixels, %i bits" % (
        len(Rawtab[0]), len(Rawtab) * len(Rawtab[0])))
    if verbose >= 1: print(
        "-=-=-=-=-=-=-=-=-=-=-=-\ntesting all variation\n-=-=-=-=-=-=-=-=-=-=-=-")

    for sens in range(sens_lecture):
        if sens == 1:
            if verbose >= 1: print("-=-=-Trying the reverse order-=-=-")
            newRawtab = []
            for band in Rawtab:
                newRawtab.append(band[::-1])
            Rawtab = newRawtab
        if verbose >= 2: print("RawTab: ", Rawtab)
        myvar = []
        while len(myvar) <= len(myrgb):
            myvar = nextvar(myvar, myrgb, verbose=verbose,
                            values=values)  # Test la prochaine variation [0]=Red , [0,1,2,3]=RGBA
            if myvar == False:
                break
            myraw = []
            for i in range(len(Rawtab[
                                   0])):  ##############################Voir pour ajouter une lecture dans l'autre sens si on preleve plusieurs bit dans une bande d'un pixel
                for j in myvar:
                    for bit in range(8):  # Add an entry for each bit ticked
                        if values[j][5][bit].get() == 1:
                            mask = 1 << (7 - bit)
                            myraw.append((Rawtab[j][i] & mask) >> (7 - bit))
            for one_bit_every in range(1, 4):  # taking one bit every ... bits
                myraw = myraw[::one_bit_every]
                # Deleting the offset bits
                for starting_at in range(8):
                    myraw = myraw[starting_at:]
                    mydesc = ""  # Version imprimable de myvar
                    for i in myvar:
                        mydesc += myrgb[i][1] + ":"
                    for bit_per_pixel in [7, 8]:
                        for bits_arrangement in [[7, 6, 5, 4, 3, 2, 1, 0],
                                                 [0, 1, 2, 3, 4, 5, 6, 7]]:
                            for xoring in [False, True]:
                                my_final_raw = []
                                if xoring:
                                    for bit in myraw:
                                        my_final_raw.append(bit ^ 1)
                                else:
                                    my_final_raw = myraw
                                if verbose >= 2:
                                    print("testing ", mydesc, "(offset ",
                                          starting_at, "-", bit_per_pixel,
                                          "b/char - 1/", one_bit_every,
                                          "bits - ", bits_arrangement,
                                          " XORing input : ", xoring, ")",)
                                data = get_valuable_data_from_tab(my_final_raw,
                                                                  alphabet=alphabet,
                                                                  min_char_length=min_char_length,
                                                                  bit_per_pixel=bit_per_pixel,
                                                                  bits_arrangement=bits_arrangement,
                                                                  filepath=filepath,
                                                                  verbose=verbose)
                                if len(data) > 0:
                                    if verbose >= 1:
                                        if verbose == 1: print(
                                            "testing ", mydesc, "(offset ",
                                            starting_at, "-", bit_per_pixel,
                                            "b/char - 1/", one_bit_every,
                                            "bits - ", bits_arrangement, ")",)
                                        print("*** MATCH FOUND *** %s : %s" % (
                                            mydesc, data))
                                    data += "*** MATCH FOUND *** %s : %s\n" % (
                                        mydesc, data)
                                else:
                                    if verbose >= 2:
                                        print("No match")
                                        data += "No match\n"
    return Rawtab, data

init_image_values()
lsb_meganalyse(main_filepath, None, image_values)
