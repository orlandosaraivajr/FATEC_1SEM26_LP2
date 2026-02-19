# aluno é uma classe, ou seja, um molde para criar objetos do tipo aluno
class Aluno:
    # nome, curso, nota_1, nota_2 e nota_3 são atributos da classe Aluno
    nome = ''
    curso = ''
    nota_1 = 0
    nota_2 = 0
    nota_3 = 0
    
    def atribuir_nome(self, nome):
        self.nome = nome
    
    def atribuir_curso(self, curso):
        self.curso = curso
    
    def atribuir_nota_1(self, nota):
        if nota < 0 or nota > 10:
            print('Nota inválida. A nota deve ser entre 0 e 10.')
        else:
            self.nota_1 = nota
        
    def atribuir_nota_2(self, nota):
        if nota < 0 or nota > 10:
            print('Nota inválida. A nota deve ser entre 0 e 10.')
        else:
            self.nota_2 = nota
        
    def atribuir_nota_3(self, nota):
        if nota < 0 or nota > 10:
            print('Nota inválida. A nota deve ser entre 0 e 10.')
        else:
            self.nota_3 = nota

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.nome + ' - ' + self.curso

#' jose e maria são objetos da classe Aluno    
jose = Aluno()
maria = Aluno()
joao = Aluno()

joao.atribuir_nome('João')
joao.atribuir_curso('Inteligência Artificial')
joao.atribuir_nota_1(4)

print(joao)
