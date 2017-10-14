SRC_DIR = .
OBJ_DIR = .
SRC = $(wildcard $(SRC_DIR)/*.c)
OBJ = $(patsubst %.c, $(OBJ_DIR)/%.o, $(notdir $(SRC)))

CC = gcc
CFLAGS = -Wall -Wextra -O1 -g
LDFLAGS =

EXEC = exploit


.PHONY: $(SRC_DIRS)

$(EXEC): $(OBJ)
	$(CC) -o $@ $(OBJ) $(CFLAGS) $(LDFLAGS)

$(OBJ_DIR)/%.o: %.c
	$(CC) -o $@ -c $< $(CFLAGS)

run: $(EXEC)
	./$(EXEC)

clean :
	@rm -rf $(EXEC)
