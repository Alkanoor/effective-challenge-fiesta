OBJ_DIR = obj
SRC_DIR = .
SRC = $(filter-out ./victory.cpp,$(shell find . -name '*.cpp'))
OBJ = $(patsubst %.cpp, $(OBJ_DIR)/%.o, $(notdir $(SRC)))
BIN = $(patsubst %.cpp, %, $(notdir $(SRC)))
VICTORY = $(OBJ_DIR)/victory.o
VPATH=.


CC = g++
CFLAGS = -Wall -O1 -std=c++11
LDFLAGS =


all: createDir $(BIN)


$(OBJ_DIR)/%.o: %.cpp
	$(CC) -o $@ -c $< $(CFLAGS)

$(BIN): %: $(OBJ_DIR)/%.o $(VICTORY)
	$(CC) -o $@ $(OBJ_DIR)/$@.o $(VICTORY) $(LDFLAGS)

createDir:
	@mkdir -p $(OBJ_DIR)

clean :
	@rm -rf $(OBJ_DIR)
	@rm -rf $(BIN)
