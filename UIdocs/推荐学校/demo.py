from flask import Flask, request, render_template,redirect,flash
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,FileField,TextField,SubmitField,\
    SelectField,SelectMultipleField
from wtforms.validators import DataRequired

app=Flask(__name__)
app.secret_key='123456'


class MyForm(FlaskForm):
    name=StringField('高考排名',validators=[DataRequired('必填')])
    #province
    my_file=SelectField(label='目前所在省份',choices=[("省份1",'省份1'),(2,'省份2'),(3,'省份3')])
    infor=SelectMultipleField(label='想去的省份',choices=[("省份1",'省份1'),(2,'省份2'),(3,'省份3'),(4,'4'),
                                                     (5,'5'),(6,'6'),(7,'7')])
    is_fav=BooleanField('是否想去双一流')
    is_f=BooleanField('是否只想去一本')
    submit=SubmitField('提交')


@app.route('/success')
def success():
    return "提交成功"
#{'name': '2', 'my_file': '1', 'infor': ['2'], 'is_fav': True, 'is_f': False, 'submit': True,
@app.route('/submit',methods=('GET','POST'))
def submit():
    form = MyForm()
    data=form.data

    if data['submit']:
        print(data)
        flask_msg="高考排名："+data['name']
        flash(flask_msg,'ok')
        flask_msg="目前所在省份："+data['my_file']
        flash(flask_msg,'ok')
        flask_msg="想去的省份："+data['infor'][0]
        flash(flask_msg,'ok')
        if data['is_fav']:
            flask_msg="是否想去双一流："+"是"
            flash(flask_msg,'ok')
        else:
            flask_msg="是否想去双一流："+"否"
            flash(flask_msg,'ok')
        if data['is_f']:
            flask_msg="是否只想去一本："+"是"
            flash(flask_msg,'ok')
        else:
            flask_msg="是否只想去一本："+"否"
            flash(flask_msg,'ok')


        #return redirect('/success')
        return render_template('submit2.html',form=form)

    return render_template('submit.html',form=form)
