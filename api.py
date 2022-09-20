from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'titulo': 'A Coisa',
        'autor': 'Stephen King'
    },

    {
        'titulo': 'O Hobbit',
        'autor': 'JRR Tolkien'
    }
]


@app.route('/livros', methods=['GET'])
def obter_todos_os_livros():
    return jsonify(livros)


@app.route('/livros/<int:livro_id>', methods=['GET'])
def obter_livro_por_id(livro_id):
    return jsonify(livros[livro_id])


def novo_livro():
    pass


def atualizar_livro():
    pass


def excluir_livro():
    pass


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
