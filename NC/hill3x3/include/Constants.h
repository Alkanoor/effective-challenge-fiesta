#ifndef CONSTANTS_H
#define CONSTANTS_H


#include <vector>
#include <string>
#include <map>

typedef std::vector<int> Vec;
typedef std::vector<Vec> Matrix;


namespace Utils
{
    std::string clean(const std::string& msg);

    std::vector<int> convert_alpha_to_num(const std::string& m);
    std::string vigenere(const std::string& charset, const std::string& msg, const std::vector<int>& offsets, bool direction);
    std::string permutation(const std::string& charset, const std::string& msg, const std::vector<int>& permut, bool direction);

    std::map<char, int> map_from_charset(const std::string& charset);
    template <typename T, typename U>
    std::map<U,T> inverse_map(const std::map<T,U>& m);
    template <typename T, typename U>
    std::map<U,std::vector<T> > inverse_map_accumulate(const std::map<T,U>& m);

    std::map<char, int> count(const std::string& msg);
    float IC(const std::string& txt);

    Matrix convert_string_to_mat(const std::string& txt, const std::map<char, int>& convertion_map, unsigned int M, unsigned int N, bool vertical = true);
    std::string convert_mat_to_string(const Matrix& mat, const std::map<int, char>& convertion_map, bool vertical = true);

    int inverseMod36(int a);
    Matrix rescaleMod36(const Matrix& m);
    Matrix prod(const Matrix &m1, const Matrix &m2);
    int det(const Matrix &mat);
    Matrix inverse(const Matrix &mat);
}


template <typename T, typename U>
std::map<U,T> Utils::inverse_map(const std::map<T,U>& m)
{
    std::map<U,T> ret;
    for(auto p : m)
        ret[p.second] = p.first;
    return ret;
}

template <typename T, typename U>
std::map<U,std::vector<T> > Utils::inverse_map_accumulate(const std::map<T,U>& m)
{
    std::map<U,std::vector<T> > ret;
    for(auto p : m)
        ret[p.second].push_back(p.first);
    return ret;
}


static std::string known_text2 = "LEQUITATIONETHOLOGIQUEAUSSIAPPELEEEQUITATIONNATURELLEESTLEDRESSAGEEQUESTREINSPIREDELETHOLOGIEEQUINECONSISTANTAINTERAGIRAVECUNCHEVALTOUTENPRENANTENCOMPTELESPARTICULARITESPSYCHOLOGIQUESDELANIMALELLECONNAITUNEVAGUEDENGOUEMENTDANSLESPAYSOCCIDENTAUXGRACEAEQUITATIONETHOLOGIQUEAUSSIAPPELEEEQUITATIONNATURELLEESTLEDRESSAGEEQUESTREINSPIREDELETHOLOGIEEQUINECONSISTANTAINTERAGIRAVECUNCHEVALTOUTENPRENANTENCOMPTELESPARTICULARITESPSYCHOLOGIQUESDELANIMALELLECONNAITUNEVAGUEDENGOUEMENTDANSLESPAYSOCCIDENTAUXGRACEAUX";
static std::string known_text = "DUNTEXTEUNAUTREONCONSTATEQUILYADESVARIATIONSSENSIBLESDELAFRQUENCEDESLETTRESYCOMPRISPOURDESTEXTESDEPLUSDELETTRESCOMMECELUIUTILISPARFRANCISLEBOUTTEPOUROBTENIRDESSTATISTIQUESAUSSIREPRSENTATIVESQUEPOSSIBLEONUTILISELECORPUSDETHOMASTEMPQUIVISEAVOIRUNVOLUMECRITIQUEETCONTENIRDESTEXTESDORIGINESDIVERSESPOURDPASSERCESPROBLMESLAPLUPARTDESANALYSESFRQUENTIELLESDELALANGUEFRANAISENETIENNENTCOMPTEQUEDESLETTRESETNONDESCARACTRESDEPONCTUATIONORCESDERNIERSSONTPLUSFRQUENTSQUECERTAINESLETTRESILFAUTDONCENTENIRCOMPTEONRE";
static std::string known_text_ciphered;
static std::string known_text_ciphered2;
static std::string target_text;
static std::string target_text_ciphered = "ZTMXQ FGTES DSSS7 43TDR 74YET GS1AG 3GA0S 0DPV5 FW5EV 3FG35 381TT CTHH4 X0T19 3GMWC X5Z1S E49IY CJ4QI CCV7V E55SV MH4P2 XK2E3 0UZY1 VM3U5 M6KL3 VHTE9 I7RSW 9ZB1Y S5RX6 0LEEI YC5RV QKGQ0 7TGS1 AG47X SA213 QETMD CFE25 3D5O0 T3E3V OUZ5E J5X4Y ED7QX QRGGB OKGE2 5F7CR U1J5X R2FB1 YO4HA 3A5EV VHT7K K81KE KPGQY TLUZ1 V8505 F8QSM ZE4X6 0TU6T CTEQP 5EMGQ Y1S56 BT0EE 51SIC C0S04 85E7G NHCFU TRU1J 5X9KV ZT5S5 251SE 55Z7B JQ1AE SXYTV 7VQY1 SJJM4 E1JM1 93PWM GRDG0 Y91XE Q38DM EVA4C QALE4 5RTEQ GHGNH HKCLI UFEE5 558YA FPQMD 8F2JR 1TQ2G KGUQ1 45C13 M8F9M QKY8I UFX2N 6VWSP VN3CQ DW8EQ FH0GM W3SIS PVHNT HC1D7 Q";

static std::map<char, int> chr_to_int_map;
static std::map<int, char> int_to_chr_map;

static Matrix matrix;


#endif
