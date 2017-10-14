OBJ_DIR = obj
SRC_DIR = .
OBJ_DIR_C = obj_c
SRC_DIR_C = spoof_crc
SRC = $(wildcard $(SRC_DIR)/*.cpp)
OBJ = $(patsubst %.cpp, $(OBJ_DIR)/%.o, $(notdir $(SRC)))
SRC_C = $(wildcard $(SRC_DIR_C)/*.c)
OBJ_C = $(patsubst %.c, $(OBJ_DIR_C)/%.o, $(notdir $(SRC_C)))
TARGET = final

CC = g++
CC_C = gcc
CFLAGS = -Wall -Werror -Wextra -O1 -std=c++14
CFLAGS_C = -Wall -Wextra -O1
LDFLAGS =


all: $(TARGET)

obj: createDir $(OBJ) $(OBJ_C)

$(TARGET): createDir $(OBJ) $(OBJ_C)
	$(CC) -o $@ $(OBJ) $(OBJ_C) $(CFLAGS) $(LDFLAGS)

$(OBJ_DIR)/%.o: %.cpp
	$(CC) -o $@ -c $< $(CFLAGS)

$(OBJ_DIR_C)/%.o: $(SRC_DIR_C)/%.c
	$(CC_C) -o $@ -c $< $(CFLAGS_C)

createDir:
	@mkdir -p $(OBJ_DIR)
	@mkdir -p $(OBJ_DIR_C)

clean :
	@rm -rf $(OBJ_DIR)
	@rm -rf $(OBJ_DIR_C)
	@rm -rf $(TARGET)
