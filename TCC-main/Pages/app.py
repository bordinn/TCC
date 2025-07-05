from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Garante que a pasta de uploads exista
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')

    if file and file.filename.endswith(('.xls', '.xlsx')):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'ultimo_upload.xlsx')
        file.save(filepath)
        print(f"[INFO] Arquivo salvo em: {filepath}")

        try:
            df = pd.read_excel(filepath)
            print("[INFO] Conteúdo do DataFrame:")
            print(df.head())

            df.to_pickle('dados_temp.pkl')
            print("[INFO] Arquivo dados_temp.pkl criado com sucesso")
        except Exception as e:
            print(f"[ERRO] Falha ao processar arquivo Excel: {e}")
            return "Erro ao processar o arquivo Excel. Verifique o arquivo enviado."

        return redirect(url_for('dados'))

    print("[WARN] Formato de arquivo inválido ou arquivo não enviado")
    return 'Formato de arquivo inválido. Envie .xls ou .xlsx'

@app.route('/dados')
def dados():
    if os.path.exists('dados_temp.pkl'):
        df = pd.read_pickle('dados_temp.pkl')
        registros = df.to_dict(orient='records')
        bonus = round(df['Projetos Concluídos'].sum() * 100, 2)
    else:
        registros = []
        bonus = 0

    return render_template('dados.html', dados=registros, bonus=bonus)

if __name__ == '__main__':
    app.run(debug=True)
