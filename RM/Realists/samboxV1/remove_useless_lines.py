with open('output', 'rb') as f:
    content = f.read().split('\n')

    with open('clear_output', 'wb') as g:
        for i in content:
            if len(i.split('00'))< 10:
                g.write(i+'\n')
