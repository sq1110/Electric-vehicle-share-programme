from flask import Flask,render_template, request, jsonify
# import pandas as pd
import db
app = Flask(__name__)

@app.route('/get_vehicle_type_data')
def get_vehicle_type_data():
    res = db.query("select vehicle_type, count(*) as total from rentinfo group by vehicle_type")
    result = []
    for item in res:
        result.append({'name':item[0].strip(), 'value':item[1]})
    print(result)
    return jsonify({'result': result})


@app.route('/get_location_data')
def get_location_data():
    res = db.query("select location, count(*) as total from rentinfo group by location order by total desc")
    x_data = []
    y_data = []
    for item in res:
        x_data.append(item[0])
        y_data.append(item[1])
    print(x_data, y_data)
    return jsonify({ 'x_data':x_data, 'y_data':y_data })


@app.route('/get_fee_data')
def get_fee_data():
    sql = '''SELECT fee_range, count(*) AS number
            FROM
                (select case when fee >= 0 and fee <= 19.99 then '0 - 20'
                when fee >= 20 and fee <= 39.99 then '20 - 40'
                when fee >= 40 and fee <= 59.99 then '40 - 60'
                when fee >= 60 and fee <= 79.99 then '60 - 80'
                when fee >= 80 and fee <= 99.99 then '80 - 100'
                else '100+ '
                end as fee_range
                FROM rentinfo
                WHERE 1
            ) AS  fee_summaries
            GROUP BY fee_range
            ORDER BY fee_range;
    '''
    res = db.query(sql)
    x_data = []
    y_data = []
    for item in res:
        x_data.append(item[0])
        y_data.append(item[1])
    # print(x_data, y_data)
    return jsonify({ 'x_data':x_data, 'y_data':y_data })


@app.route('/get_hour_data')
def get_hours_data():
    sql = '''SELECT hour_range, count(*) AS number
            FROM
                (select case when hours >= 0 and hours <= 0.99 then '0 - 1'
                when hours >= 1 and hours <= 2.99 then '1 - 2'
                when hours >= 2 and hours <= 3.99 then '2 - 3'
                when hours >= 3 and hours <= 4.99 then '3 - 4'
                when hours >= 5 and hours <= 6.99 then '5 - 6'
                else '7+ '
                end as hour_range
                FROM rentinfo
                WHERE 1
            ) AS  hour_summaries
            GROUP BY hour_range
            ORDER BY hour_range;
    '''
    res = db.query(sql)
    x_data = []
    y_data = []
    for item in res:
        x_data.append(item[0])
        y_data.append(item[1])
    # print(x_data, y_data)
    return jsonify({ 'x_data':x_data, 'y_data':y_data })
        
    return jsonify({'result': result})


# index page
@app.route('/')
def index():
    return render_template('vehicle_type.html')


@app.route('/vehicletype')
def brand():
    return render_template('vehicle_type.html')

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/hour')
def hour():
    return render_template('hour.html')

@app.route('/fee')
def fee():
    return render_template('fee.html')

if __name__ == '__main__':
    app.run(port=8080,debug=True)

