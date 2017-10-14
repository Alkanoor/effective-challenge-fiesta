#ifndef SPOOF_H
#define SPOOF_H


#ifdef __cplusplus
extern "C" {
#endif

#include "fline.h"


void warn(const char *why);
void fail(const char *why);
void *alloc(void *space, size_t size);


typedef unsigned long long word_t;
typedef unsigned long long range_t;
#define WORDFMT "llx"
#define RANGEFMT "llu"
#define WORDBITS ((int)sizeof(word_t)<<3)
#define ONES(n) (((word_t)0 - 1) >> (WORDBITS - (n)))


typedef struct {
    short dim;
    short ref;
    word_t poly;
} model_t;

struct locus {
    range_t off;
    short pos;
};

word_t crc_byte(word_t crc, unsigned val, model_t model);
word_t gf2_matrix_times(const word_t *mat, word_t vec);
void gf2_matrix_square(word_t *square, const word_t *mat, int dim);

const word_t *crc_zeros_operator(int k, model_t model);
word_t crc_zeros(word_t crc, range_t len, model_t model);
word_t crc_sparse(const struct locus *loci, int locs, range_t len,
                        model_t model);

int gf2_matrix_solve(word_t *x, const word_t *M, word_t c, int rows,
                           int cols);
int crc_solve(struct locus *loci, int locs, range_t len, word_t want,
                    model_t model);

int locus_order(const void *a, const void *b);

int decimal_digits(range_t n);
char *getinput(fline_t *state);


#ifdef __cplusplus
}
#endif

#endif
