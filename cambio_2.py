import tkinter as tk

class ChessGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Game")
        self.geometry("400x400")
        
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        
        self.selected_piece = None
        self.create_board()
        
    def create_board(self):
        for i in range(8):
            for j in range(8):
                label = tk.Label(self, text=self.board[i][j], font=("Arial", 16))
                label.grid(row=i, column=j, padx=5, pady=5)
                label.bind("<Button-1>", lambda event, row=i, col=j: self.on_click(row, col))
                
    def on_click(self, row, col):
        if not self.selected_piece:
            piece = self.board[row][col]
            if piece != ' ':
                self.selected_piece = (row, col)
        else:
            self.move_piece(row, col)  # Llamada al m�todo move_piece

    # Cambio2
    def move_piece(self, row, col):
        selected_row, selected_col = self.selected_piece
        piece = self.board[selected_row][selected_col]
        self.board[selected_row][selected_col] = ' '
        self.board[row][col] = piece
        self.selected_piece = None
        self.refresh_board()  # Llamada al m�todo refresh_board

    def refresh_board(self):
        # Agregar l�gica para actualizar la interfaz gr�fica con el nuevo estado del tablero
        pass  # Por ahora, no se implementa la actualizaci�n gr�fica

chess_game = ChessGame()
chess_game.mainloop()


