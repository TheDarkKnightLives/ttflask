from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        num_subjects = int(request.form['numSubjects'])
        subjects = []
        
        for i in range(num_subjects):
            subject_name = request.form[f'subjectName{i}']
            hours = int(request.form[f'hours{i}'])
            is_static = request.form.get(f'static{i}', False) == 'on'
            
            static_info = []
            if is_static:
                for j in range(hours):
                    day = int(request.form[f'day{i}_{j}'])
                    period = int(request.form[f'period{i}_{j}'])
                    static_info.append({'day': day, 'period': period})

            subjects.append({
                'name': subject_name,
                'hours': hours,
                'static': is_static,
                'static_info': static_info
            })

        return render_template('index.html', subjects=subjects)

    return render_template('index.html', subjects=[])

if __name__ == '__main__':
    app.run(debug=True)
