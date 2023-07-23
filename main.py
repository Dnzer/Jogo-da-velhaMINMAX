import tkinter as tk
from tkinter import messagebox
import random

class JogoDaVelha:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Velha")
        self.jogador_atual = "X"
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        self.menu()
        self.criar_interface("Human",False)
        self.partida = True


    def centralComando(self):

        tela=tk.Tk()
        tela.title("Central de jogadas")
        tela.geometry("300x180")

        linhaInput = tk.IntVar(name='int')
        colunaInput = tk.IntVar(name='int')

        linha =tk.IntVar()
        coluna =tk.IntVar()

        labelLinha = tk.Label(tela, text="linha")
        labelLinha.pack()

        linhaInput=tk.Entry(tela, textvariable=linha)
        linhaInput.pack()

        labelColuna = tk.Label(tela, text="Coluna")
        labelColuna.pack()

        colunaInput=tk.Entry(tela, textvariable=coluna)# , textvariable=self.coluna
        colunaInput.pack()





        bt_jogada=tk.Button(tela,text='MARCAR',command=lambda :self.fazer_jogadaMachine(linhaInput.get(),colunaInput.get()))
        bt_jogada.pack()








        tela.mainloop()

    def criar_interface(self,valor_modo,apagar):
        if apagar:
            self.frame.destroy()
            apagar=False

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        if valor_modo=='Human':
            for i in range(3):
                for j in range(3):
                    self.botoes[i][j] = tk.Button(
                        self.frame, text=' ', width=10, height=5,
                        command=lambda i=i, j=j: self.fazer_jogada(i,j)
                    )

                    self.botoes[i][j].grid(row=i, column=j)
        else:
            print("-------HOMEM VS MÁQUINA---------")
            for i in range(3):
                for j in range(3):
                    self.botoes[i][j] = tk.Button(
                        self.frame, text=' ', width=10, height=5,state=tk.DISABLED)
                    self.botoes[i][j].grid(row=i, column=j)


            self.centralComando()



    def fazer_jogadaMachine(self,linha,coluna):

        i=int(linha)
        j=int(coluna)
        print("fazer_jogadaMachine!!!")

        if self.tabuleiro[i][j] == ' ':
            self.tabuleiro[i][j] = self.jogador_atual
            self.botoes[i][j].config(text=self.jogador_atual)
            print("--------------------")
            print("Jogador",self.jogador_atual)
            print("linha",i)
            print("coluna",j)
            print("--------------------")
            if self.verificar_vitoria():
                messagebox.showinfo("Fim de jogo", f"O jogador {self.jogador_atual} venceu!")
                self.reiniciar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo("Fim de jogo", "Empate!")
                self.reiniciar_jogo()

            else:
                self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'
                if self.jogador_atual=='O':
                    print("------JOGADA MACHINE----------------")
                    linha=random.randint(0,2)
                    coluna=random.randint(0,2)
                    self.fazer_jogadaMachine(linha,coluna)

        else:
            if self.jogador_atual=="O":
                linha=random.randrange(0,2)
                coluna=random.randrange(0,2)
                self.fazer_jogadaMachine(linha,coluna)
            print("POSIÇÃO INVALIDA TENTE NOVAMENTE")









    def fazer_jogada(self, linha, coluna):
        print("Fazer_jogada")

        if self.tabuleiro[linha][coluna] == ' ':
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.botoes[linha][coluna].config(text=self.jogador_atual)
            print("Jogador",self.jogador_atual)
            print("linha",linha)
            print("coluna",coluna)
            print("--------------------")
            if self.verificar_vitoria():
                messagebox.showinfo("Fim de jogo", f"O jogador {self.jogador_atual} venceu!")
                self.reiniciar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo("Fim de jogo", "Empate!")
                self.reiniciar_jogo()
            else:
                self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'
        else:
            print("POSIÇÃO INVALIDA TENTE NOVAMENTE")


    def verificar_vitoria(self):
        # Verificar linhas
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != ' ':
                return True
        # Verificar colunas
        for j in range(3):
            if self.tabuleiro[0][j] == self.tabuleiro[1][j] == self.tabuleiro[2][j] != ' ':
                return True
        # Verificar diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != ' ':
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ' ':
            return True
        return False

    def verificar_empate(self):
        for linha in self.tabuleiro:
            if ' ' in linha:
                return False
        return True

    def reiniciar_jogo(self):
        for i in range(3):
            for j in range(3):
                self.tabuleiro[i][j] = ' '
                self.botoes[i][j].config(text=' ')

        self.jogador_atual = 'X'


    def conf_Modo(self,value_inside):
        #resposta = messagebox.askyesno("Configuração de modo", "Deseja mudar o adversário?")

        #if resposta:
            messagebox.showinfo("Modo alterado", "O jogo será reiniciado")

            self.reiniciar_jogo()

            apagar=True
            print("Comando executado!")

        #else:
            #print("Comando cancelado.")

            #if(value_inside=='Human'):
                #print("entrou no if")


            #else:
                #print("entrou no else")
            print("valor do value: ",value_inside)
            self.criar_interface(value_inside,apagar)

    def Select_modo(self,janela):
        options_list = ["Human", "Machine"]

        # Variable to keep track of the option
        # selected in OptionMenu

        #value_inside = tk.StringVar(root)
        value_inside = tk.StringVar()
        modo_atual= tk.StringVar()


        # Set the default value of the variable
        value_inside.set(options_list[0])  # definindo como valor padrão Human

        # Create the optionmenu widget and passing
        # the options_list and value_inside to it.

        #pegando o valor atual da escolha do modo
        auxMod=value_inside.get()
        modo_atual.set(auxMod)
        print("value_inside antes da escolha: ",modo_atual.get())
        #print("value_inside antes da escolha: ", value_inside.get())

        question_menu = tk.OptionMenu(root,value_inside, *options_list,command=self.conf_Modo)

        question_menu.place(x=173, y=2.5)
        print("value_inside depois da escolha",value_inside.get())





    def menu(self):
        ##########Botões#######
        gerarArvore = tk.Button(root, text='ÁRVORE',command=self.arvore)
        melhor_jogada = tk.Button(root, text='DICA',command=self.melhorJogada)#
        NovoJogo = tk.Button(root, text='NOVO JOGO', command=self.reiniciar_jogo)
        melhor_jogada.place(x=2, y=5)
        gerarArvore.place(x=40, y=5)
        NovoJogo.place(x=95, y=5)
        self.Select_modo(root)

    def desenhaNo(self,canvas,tag, nivel,eixoX,eixoY):


        if nivel==9: #ou seja a primeira jogada
            #procurar um jeito de centralizar esse nodo indepente do tamanho da tela!

            linha_horizontal1 = canvas.create_line(25, 70, 175, 70)
            linha_horizontal2 = canvas.create_line(25, 140, 175, 140)
            linha_vertical1 = canvas.create_line(65, 25, 65, 175)
            linha_vertical2 = canvas.create_line(130, 25, 130, 175)

            #canvas.create_oval(10, 10, 190, 190, outline='black')
            eixoX2=eixoX+180
            eixoY2=eixoY+180
            canvas.create_oval(eixoX,eixoY,eixoX2,eixoY2, outline='black')
            # indicador de qual estado a busca está
            canvas.create_text(eixoX2, eixoY, text=str(tag), fill='blue')

            # mapeando os campos do jogo da velha
            # linha 1 do jogo da velha
            canvas.create_text(35, 45, text='00', fill='green')
            canvas.create_text(98, 45, text='01', fill='red')
            canvas.create_text(161, 45, text='02', fill='green')
            # linha 2 do jogo da velha
            canvas.create_text(35, 89, text='10', fill='green')
            canvas.create_text(98, 89, text='11', fill='red')
            canvas.create_text(161, 89, text='12', fill='green')
            # linha 3 do jogo da velha
            canvas.create_text(35, 150, text='10', fill='green')
            canvas.create_text(98, 150, text='11', fill='red')
            canvas.create_text(161, 150, text='12', fill='green')

            canvas.pack()
    def arvore(self):
        janela2 = tk.Tk()
        #janela2.geometry("300x300")

        # Criando o Canvas
        canvas = tk.Canvas(janela2)
        #canvas.pack()
        #canvas.pack(expand=True)

        # Criando a Scrollbar
        scrollbarX=tk.Scrollbar(janela2,orient='horizontal',command=canvas.xview)#
        scrollbarX.pack(side=tk.BOTTOM,fill=tk.X)

        scrollbarY= tk.Scrollbar(janela2,orient='vertical',command=canvas.yview)#,command=canvas.yview()
        scrollbarY.pack(side=tk.RIGHT,fill=tk.Y)#fill=tk.Y

        # Configurando a Scrollbar para controlar o Canvas
        canvas.configure(xscrollcommand=scrollbarX.set)
        canvas.configure(yscrollcommand=scrollbarY.set)

        # Criando um Frame para conter os widgets
        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame)#anchor=tk.NW



        # Configurando a rolagem do Canvas
        def on_canvas_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))


        canvas.bind("<Configure>", on_canvas_configure)

# DESENHANDO UM NODO DA ARVORE!!!!!!
#___________________________________________________________________________________
        nivel = 9
        tag = 'Max'
        posicaoX = 100
        posicaoY = 100
        self.desenhaNo(canvas, tag, nivel, posicaoX, posicaoY)
        posicaoX = -10
        posicaoY = 10
        tag = "Min"
        self.desenhaNo(canvas, tag, nivel, posicaoX, posicaoY)

        posicaoX = 300
        posicaoY = 30
        tag = "AAAAAAA"
        self.desenhaNo(canvas, tag, nivel, posicaoX, posicaoY)

        posicaoX = 700
        posicaoY = 500
        tag = "BBBBBBBBBBB"
        self.desenhaNo(canvas, tag, nivel, posicaoX, posicaoY)






        janela2.title("Árvore de Jogadas")
        janela2.mainloop()



    def melhorJogada(self):
        dica = tk.Tk()

        frame = tk.Frame(dica)
        frame.pack()

        botoes = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                botoes[i][j] = tk.Button(
                    frame, text='aaaaaaaa', width=10, height=5,

                )
                botoes[i][j].grid(row=i, column=j)

        dica.title("Dica")

        dica.mainloop()




root = tk.Tk()

canvas = tk.Canvas(root)
canvas = tk.Canvas(root, width=250, height=30)  # definindo tamanhoda view
canvas.pack()
jogo = JogoDaVelha(root)



root.mainloop()
