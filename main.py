from flask import Blueprint, render_template, flash,request,redirect,url_for,send_file
from flask_login import login_user, logout_user, login_required, current_user
from __init__ import create_app, db
from models import Station,User,AME,FlightNO

import calendar
from datetime import datetime,timedelta

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sqlalchemy.sql import func

# our main blueprint
main = Blueprint('main', __name__)

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')
#////////////////////////////////////////////////////////////////////////////////////////////////
@main.route('/profile') # profile page that return 'profile'
@login_required
def profile():
    if current_user.name == 'Karachi' or current_user.name == 'Islamabad' or current_user.name == 'Multan' or current_user.name == 'Peshawar' or current_user.name == 'Faisalabad' or current_user.name == 'Quetta' or current_user.name=='Lahore':
        ntstation = Station.query.filter_by(station=current_user.name)
        allame = AME.query.all()
        allflt = FlightNO.query.all()
        return render_template('profile.html',name=current_user.name,ntstation=ntstation,email=current_user.email,allame=allame,allflt=allflt)
    else:
        logout_user()
        return redirect(url_for('main.index'))
#////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////
@main.route('/profile1',methods=['POST']) # profile page that return 'profile'
@login_required
def profile1():
    try:
        operator = request.form['operator']
        station=current_user.name
        date = request.form['date']
        acreg = request.form['acreg']
        fltno = request.form['fltno']
        actype = request.form['actype']
        sector = request.form['sector']
        sta = request.form['sta']
        std = request.form['std']
        ata = request.form['ata']
        atd = request.form['atd']
        aircraftcheck = request.form['aircraftcheck']
        defect = request.form['defect']
        rectification = request.form['rectification']
        delay = request.form['delay']
        engineer = request.form['engineer']
        technician = request.form['technician']
        status=request.form['status']
        comment = request.form['comment']
        now = datetime.now()
        month_name = now.strftime('%B')
        year = now.year
        month = f'{month_name} {year}'
        # user = Station.query.filter_by(date=date, fltno=fltno)
        # if user:
        #    s='This Data or Record already exists'
        #    return render_template('profile.html',s=s)

        new_user = Station(operator, station, date, acreg, fltno,
                           actype, sector, sta, std, ata, atd,
                           aircraftcheck,
                           defect, rectification, delay, engineer,
                           technician,
                           month, status,comment)  # //

        db.session.add(new_user)
        ntstation = Station.query.filter_by(station=current_user.name)
        db.session.commit()
        allame = AME.query.all()
        allflt = FlightNO.query.all()

        return render_template('profile.html', name=current_user.name,ntstation=ntstation,s='Record Added Successfully',email=current_user.email,allame=allame,allflt=allflt)
    except :
        return render_template('error.html',  s="Fail to add record")
#////////////////////////////////////////////////////////////////////////////////////////////////



#//////////////////////////////////showForStation//////////////////////////////////////////////////////////////
@main.route('/update/<string:date>/<string:fltno>', methods=['GET', 'POST'])
@login_required
def show_update(date, fltno):
    row = Station.query.filter_by(date=date, fltno=fltno)     #.first()
    return render_template("profile.html")

#////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////Email//////////////////////////////////////////////////////////////
@main.route('/emailme', methods=['GET', 'POST'])
@login_required
def emailme():
    operator = request.form['operator']
    station = current_user.name
    date = request.form['date']
    acreg = request.form['acreg']
    fltno = request.form['fltno']
    actype = request.form['actype']
    sector = request.form['sector']
    sta = request.form['sta']
    std = request.form['std']
    ata = request.form['ata']
    atd = request.form['atd']
    aircraftcheck = request.form['aircraftcheck']
    defect = request.form['defect']
    rectification = request.form['rectification']
    delay = request.form['delay']
    engineer = request.form['engineer']
    technician = request.form['technician']
    status = request.form['status']
    comment = request.form['comment']
    password = request.form['password']

    # Email details
    # Update the following variables with your specific values
    sender_email = current_user.email
    receiver_email = ["imrandawntv@gmail.com", "admin@nt.com.pk"]
    cc_email = ["sulman786us@hotmail.com", "admin@nt.com.pk"]  # Update with Cc email addresses
    subject = "Arrival/Departure Report-" + operator + ',' + fltno + '_' + date + '_' + station

    message = '''<html>
    <head>
    <style>
    table {{
      width: 100%;
       border-collapse: separate;
    }}

    table, td, th {{
      border: 2px solid blue;
      padding: 8px;
    }}

    th {{
      background-color: #FDC56D;
    }}
    </style>
    </head>
    <body>
    <p style="font-size:20px"><b>Dear MCC,</p>
    <p style="font-size:18px">Details of Subject email is as follows:</p>
   
    <table>
    <tr><th> Operator</th><td><b>{}</td></tr>
    <tr><th>  Flt No.</th><td><b>{}</td></tr>
    <tr><th> Station</th><td><b>{}</td></tr>
    <tr><th> A/C Registration No.</th><td><b>{}</td></tr>
    <tr><th> STA UTC</th><td><b>{}</td></tr>
    <tr><th> STD UTC</th><td><b>{}</td></tr>
    <tr><th> ATA UTC</th><td><b>{}</td></tr>
    <tr><th> ATD UTC</th><td><b>{}</td></tr>
    <tr><th> Engineer</th><td><b>{}</td></tr>
    <tr><th> Technician</th><td><b>{}</td></tr>
    <tr><th> Delay</th><td><b>{}</td></tr>
    <tr><th> Defect</th><td><b>{}</td></tr>
    <tr><th> Rectification</th><td><b>{}</td></tr>
    <tr><th> Status</th><td><b>{}</td></tr>
    </table>
    <p style="font-size:18px">Best Regards,</p>
    </body>
    </html>
    '''

    # Connect to the SMTP server
    smtp_server = "mail.nt.com.pk"
    smtp_port = 26
    username = current_user.email
    password = password  # Replace with the actual password

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)

        # Create a multi-part message container
        message_container = MIMEMultipart('alternative')
        message_container['Subject'] = subject
        message_container['From'] = sender_email
        message_container['To'] = ', '.join(receiver_email)
        message_container['Cc'] = ', '.join(cc_email)

        # Add HTML content to the message
        html_content = MIMEText(
            message.format(operator,fltno,station,acreg, sta, std, ata, atd, engineer, technician, delay, defect, rectification, status),
            'html')
        message_container.attach(html_content)

        # Send the email
        server.sendmail(sender_email, receiver_email + cc_email, message_container.as_string())

        # flash('Email sent successfully!')

    except Exception as e:
        s = f'Error: {str(e)}'
        print(f'Error: {str(e)}')
        return render_template('error.html', s=s)


    finally:
        # Disconnect from the server
        server.quit()

    return redirect(url_for('main.profile'))
#////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////EngineRoom/////////////////////////////////
@main.route('/EngineRoom', methods=['GET','POST'])
@login_required
def EngineRoom( ):
    if current_user.name == 'Admin':
      alluser = User.query.all()
      allstation=Station.query.all()
      allame = AME.query.all()
      allflt = FlightNO.query.all()
      return render_template('EngineRoom.html',alluser=alluser,allstation=allstation,allame=allame,allflt=allflt)
    else:
        logout_user()
        return redirect(url_for('main.index'))
#////////////////////////////////////////////Delete User////////////////////////////////////////////////////
# This route is for deleting our User
@main.route('/delete/<id>/', methods=['GET', 'POST'])
@login_required
def delete(id):
    my_data = User.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash(" User Deleted Successfully")

    return redirect(url_for('main.EngineRoom'))
#////////////////////////////////////////////////////////////////
#////////////////////////////////////////////Delete Flight Data////////////////////////////////////////////////////
# This route is for deleting our User
@main.route('/flightdelete/<date>/<fltno>', methods=['GET', 'POST'])
@login_required
def flightdelete(date,fltno):
    # print(fltno)
    # print(date)
    my_data = Station.query.filter_by(date=date, fltno=fltno).first()
    print(my_data)

    if my_data:
        db.session.delete(my_data)
        db.session.commit()
        flash("Flight Record Deleted Successfully")
    else:
        flash("Flight not found.")

    return redirect(url_for('main.EngineRoom'))


#////////////////////////////////////////////////////////////////
#////////////////////////////////All Updates////////////////////////////////
@main.route('/allupdate', methods=['GET', 'POST'])
@login_required
def allupdate():
    if request.method == 'POST':
        operator = request.form['operator']
        station = request.form['station']
        date = request.form['date']
        acreg = request.form['acreg']
        fltno = request.form['fltno']
        actype = request.form['actype']
        sector = request.form['sector']
        sta = request.form['sta']
        std = request.form['std']
        ata = request.form['ata']
        atd = request.form['atd']
        aircraftcheck = request.form['aircraftcheck']
        defect = request.form['defect']
        rectification = request.form['rectification']
        delay = request.form['delay']
        engineer = request.form['engineer']
        technician = request.form['technician']
        status = request.form['status']
        comment = request.form['comment']

        # Find the record to update based on date and fltno
        record = Station.query.filter_by(date=date, fltno=fltno).first()

        if record:
            # Update the record with the new values
            record.operator = operator
            record.station = station
            record.acreg = acreg
            record.actype = actype
            record.sector = sector
            record.sta = sta
            record.std = std
            record.ata = ata
            record.atd = atd
            record.aircraftcheck = aircraftcheck
            record.defect = defect
            record.rectification = rectification
            record.delay = delay
            record.engineer = engineer
            record.technician = technician
            record.status = status
            record.comment = comment

            # Commit the changes to the database
            db.session.commit()

            flash("Record Updated Successfully")
        else:
            flash("Record Not Found")

        return redirect(url_for('main.EngineRoom'))
    else:
        flash("Failed to Update Record")
        return redirect(url_for('main.EngineRoom'))

#////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////Backup Database///////////////////////////////////////////////////////
@main.route('/backup', methods=['GET'])
@login_required
def backup():
    # Check if the user is authorized to download the database
    # Add your authorization logic here
    current_date = datetime.now().strftime("%Y-%m-%d")
    # Generate a filename for the downloaded file
    filename = 'C:/Users/HP/PycharmProjects/NortekFlightOperation/instance/db.sqlite'

    # Send the file to the user for download
    return send_file(filename, as_attachment=True)
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////Monthly Report///////////////////////////////////////////////////////////////

@main.route('/monthlyreport', methods=['GET', 'POST'])
@login_required
def monthlyreport():
    operator = request.form['operator']
    station = request.form['station']
    month = request.form['month']
    monthly=db.session.query(Station).filter(Station.operator == operator, Station.station==station, Station.month==month)
    count = db.session.query(Station).filter(Station.operator == operator, Station.station==station, Station.month==month).count()

    return render_template('MonthlyReport.html', monthly=monthly, count=count,operator=operator, station=station,month=month)
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////Last week Report///////////////////////////////////////////////////////////////
@main.route('/lastweekreport', methods=['GET', 'POST'])
@login_required
def lastweekreport():
    operator = request.form['operator']
    station = request.form['station']

    # Calculate the start and end dates for the last week
    enddate = request.form['enddate']
    startdate = request.form['startdate']

    monthly=db.session.query(Station).filter(
        Station.operator == operator,
        Station.station == station,
        Station.date >= startdate,
        Station.date <= enddate
     )
    count = db.session.query(Station).filter(
    Station.operator == operator,
    Station.station == station,
    Station.date >= startdate,
    Station.date <= enddate
     ).count()

    return render_template('LastWeekReport.html', monthly=monthly,count=count,operator=operator, station=station,startdate=startdate,enddate=enddate)
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#//////////////////////////////////////////////////////////DashBoard//////////////////////////////////////////////////////////////////////
@main.route('/dash', methods=['GET', 'POST'])
@login_required
def dash():
  if current_user.name == 'Admin' or current_user.name == 'CEO' or current_user.name == 'COO' or current_user.name == 'MgrOps' or current_user.name == 'MgrLM':
    username = current_user.name
    now = datetime.now()
    month_name = now.strftime('%B')
    year = now.year
    month = f'{month_name} {year}'

    flights_count = db.session.query(
        Station.operator,
        db.func.count(Station.operator).filter(Station.month==month)).group_by(Station.operator).all()

    today = datetime.today()
    start_date = datetime(today.year, today.month - 1, 1)
    end_date = datetime(today.year, today.month, 1) - timedelta(days=1)
    lastmonth = db.session.query(
        Station.operator,
        db.func.count(Station.operator).filter(Station.date >= start_date, Station.date <= end_date)).group_by(Station.operator).all()

    current_date = datetime.now()
    last_month = current_date - timedelta(days=30)
    last_month_name = calendar.month_name[last_month.month]
    last_month_year = last_month.year

    monthlyflights = db.session.query(Station).filter(Station.month == month).order_by(Station.station)

    # Perform the query month operations by station and operator
    operatorstaionmonth = db.session.query(
        Station.operator,
        Station.station,
        func.count().label('row_count')
    ).filter( Station.month== month
    ).group_by(
        Station.operator,
        Station.station
    ).all()

    # Perform the query last month operations by station and operator
    operatorstaionlastmonth = db.session.query(
        Station.operator,
        Station.station,
        func.count().label('row_count')
    ).filter(Station.date >= start_date, Station.date <= end_date
             ).group_by(
        Station.operator,
        Station.station
    ).all()



    # Print the results
    for result in operatorstaionmonth:
        print(result.operator, result.station, result.row_count)

    return render_template('dash.html', username=username,flights_count=flights_count,month=month,lastmonth=lastmonth,last_month_name=last_month_name,last_month_year= last_month_year,monthlyflights=monthlyflights,operatorstaionmonth=operatorstaionmonth,operatorstaionlastmonth=operatorstaionlastmonth)
  else:
      logout_user()
      return redirect(url_for('main.index'))
#////////////////////////////////////////charts////////////////////////////////////////////////////////////////////////////////////////
@main.route('/chart', methods=['GET', 'POST'])
@login_required
def chart():
    now = datetime.now()
    month_name = now.strftime('%B')
    year = now.year
    month1 = f'{month_name} {year}'

    today = datetime.today()
    start_date = datetime(today.year, today.month - 1, 1)
    end_date = datetime(today.year, today.month, 1) - timedelta(days=1)
    # Perform the query
    result = db.session.query(
        ( Station.month).label('month'),
        func.count().label('count')
    ).group_by('month').all()

    currentmonth = db.session.query(
        Station.operator,
        db.func.count(Station.operator).filter(Station.month == month1)).group_by(Station.operator).all()
    lastmonth = db.session.query(
        Station.operator,
        db.func.count(Station.operator).filter(Station.date >= start_date, Station.date <= end_date)).group_by(
        Station.operator).all()
    current_date = datetime.now()
    last_month = current_date - timedelta(days=30)
    last_month_name = calendar.month_name[last_month.month]
    last_month_year = last_month.year

    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    currentweek = db.session.query(
        Station.station,Station.operator,db.func.count().label('count')
    ).filter(Station.date.between(start_of_week, end_of_week)
    ).group_by(Station.station, Station.operator).all()

    return render_template('chart.html',username=current_user.name,month=month1,result=result,currentmonth=currentmonth,lastmonth=lastmonth, last_month_name= last_month_name,last_month_year=last_month_year,currentweek=currentweek)
#///////////////////////////////////////////////////table/////////////////////////////////////////////////////////////////////////////
@main.route('/table', methods=['GET', 'POST'])
@login_required
def table():
    now = datetime.now()
    month_name = now.strftime('%B')
    year = now.year
    month = f'{month_name} {year}'
    result = (
        db.session.query(
            Station.station,
            Station.engineer,
            func.count().label('row_count')
        )
        .filter(Station.month == month)
        .group_by(Station.station, Station.engineer)
        .all()
    )
    # lastmonth Engineer work
    today = datetime.today()
    start_date = datetime(today.year, today.month - 1, 1)
    end_date = datetime(today.year, today.month, 1) - timedelta(days=1)
    # Last month Names and year Names
    current_date = datetime.now()
    last_month = current_date - timedelta(days=30)
    last_month_name = calendar.month_name[last_month.month]
    last_month_year = last_month.year

    lastmonthAMEresult = (
        db.session.query(
            Station.station,
            Station.engineer,
            func.count().label('row_count')
        )
        .filter(Station.date >= start_date, Station.date <= end_date)
        .group_by(Station.station, Station.engineer)
        .all()
    )
    lastmonthlyflights = db.session.query(Station).filter(Station.date >= start_date, Station.date <= end_date).order_by(Station.station)

    # Query the table for status current month
    statusresults = db.session.query(Station).filter(
        Station.status.in_(['CANCEL', 'DIVERT']),
         Station.month== month).all()
    # Query the table for last month status
    lastmonthstatusresults = db.session.query(Station).filter(
        Station.status.in_(['CANCEL', 'DIVERT']),
        Station.date >= start_date, Station.date <= end_date).all()
    return render_template('table.html',username=current_user.name,month=month,result=result, lastmonthAMEresult=lastmonthAMEresult,last_month_name=last_month_name,last_month_year= last_month_year,lastmonthlyflights=lastmonthlyflights,statusresults=statusresults,lastmonthstatusresults=lastmonthstatusresults)
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////Add AME's/////////////////////////////////////////////////
@main.route('/addame', methods=['GET', 'POST'])# we define the sign up path
@login_required
def addame(): # define the sign up function
    if request.method=='GET': # If the request is GET we return the page and forms
        return render_template('main.EngineRoom.html')
    else: # if the request is POST, then we check if the email doesn't already exist and then we save data
        amename = request.form.get('amename')

        ame = AME.query.filter_by(amename=amename).first() # if this returns a user, then the email already exists in database
        if ame: # if a user is found, we want to redirect back to signup page so user can try again
            flash('AME Name already exists')
            return redirect(url_for('main.EngineRoom'))
        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_ame = AME(amename=amename) #
        # add the new user to the database
        db.session.add(new_ame)
        db.session.commit()
        flash('AME Name Added Successfully')
        return redirect(url_for('main.EngineRoom'))

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////Add Flight No./////////////////////////////////////////////////
@main.route('/addflt', methods=['GET', 'POST'])# we define the sign up path
@login_required
def addflt(): # define the sign up function
    if request.method=='GET': # If the request is GET we return the page and forms
        return render_template('main.EngineRoom.html')
    else: # if the request is POST, then we check if the email doesn't already exist and then we save data
        fltno = request.form.get('fltno')

        flightno = FlightNO.query.filter_by(fltno=fltno).first() # if this returns a user, then the email already exists in database
        if flightno: # if a user is found, we want to redirect back to signup page so user can try again
            flash('Flight No. already exists')
            return redirect(url_for('main.EngineRoom'))
        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_fltno = FlightNO(fltno=fltno) #
        # add the new user to the database
        db.session.add(new_fltno)
        db.session.commit()
        flash('Flight No.  Added Successfully')
        return redirect(url_for('main.EngineRoom'))

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////Delete AME////////////////////////////////////////////////////
# This route is for deleting our AME
@main.route('/deleteame/<id>/', methods=['GET', 'POST'])
@login_required
def deleteame(id):
    my_data = AME.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash(" AME Deleted Successfully")

    return redirect(url_for('main.EngineRoom'))
#////////////////////////////////////////////////////////////////
#////////////////////////////////////////////Delete Flight No////////////////////////////////////////////////////
# This route is for deleting our AME
@main.route('/deleteflt/<id>/', methods=['GET', 'POST'])
@login_required
def deleteflt(id):
    my_data = FlightNO.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash(" Flight No. Deleted Successfully")

    return redirect(url_for('main.EngineRoom'))
#////////////////////////////////////////////////////////////////
@main.route('/workorder', methods=['GET', 'POST'])
@login_required
def workorder():
    return render_template('workorder.html')
#////////////////////////////////////////////////////////////////
app = create_app() # we initialize our flask app using the __init__.py function

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # create the SQLite database
    app.run(host="0.0.0.0") # run the flask app on debug mode
