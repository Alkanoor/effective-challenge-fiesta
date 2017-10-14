SRC_DIR = .
OBJ_DIR = .
SRC = $(wildcard $(SRC_DIR)/*.cpp)
OBJ = $(patsubst %.cpp, $(OBJ_DIR)/%.o, $(notdir $(SRC)))

CC = g++
ifdef SYSTEMROOT
CFLAGS = -Wall -Wextra -O3 -std=c++14 -DWIN32
LDFLAGS = -O3 -lcurl
else
CFLAGS = -Wall -Wextra -O3 -std=c++11 -Dlinux -D_GLIBCXX_USE_CXX11_ABI=0
LDFLAGS = -O3 -lpthread -lcurl -D_GLIBCXX_USE_CXX11_ABI=0
endif

EXEC = snaked


.PHONY: $(SRC_DIRS)

$(EXEC): $(OBJ)
	$(CC) -o $@ $(OBJ) $(CFLAGS) $(LDFLAGS)

$(OBJ_DIR)/%.o: %.cpp
	$(CC) -o $@ -c $< $(CFLAGS)

run: $(EXEC)
	./$(EXEC)

clean :
	@rm -rf $(EXEC)
	@rm -rf $(OBJ)
