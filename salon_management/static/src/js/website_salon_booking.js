odoo.define('salon_management.website_salon_booking', function (require) {
    'use strict';

    var ajax = require('web.ajax');
    var core = require('web.core');
    var _t = core._t;
    var rpc = require('web.rpc');
    var QWeb = core.qweb;

    $(document).on('click', "#submit_button", function () {
        var name = $("#name").val();
        var date = $("#date").val();
        var time = $("#time").val();
        var phone = $("#phone").val();
        var email = $("#email").val();
        var service = $('.check_box_salon:checkbox:checked');
        var chair = $("#chair").val();
        var list_service = [];
        var number = service.length;
        var time_booking = [];
        var datetimeString = `${date} ${time}`;
        var get_datetime = moment.utc(datetimeString, 'MM-DD-YYYY HH:mm').subtract(7, 'hours');
        var fix_datetime = get_datetime.format('YYYY-MM-DD HH:mm:ss');
        var today = get_datetime.diff(moment.utc(), 'hours'); 
        var salon_holiday = [];
        var day_name = get_datetime.format('ddd');
        var dayAliases = {
            'Sun': 'Sunday',
            'Mon': 'Monday',
            'Tue': 'Tuesday',
            'Wed': 'Wednesday',
            'Thu': 'Thursday',
            'Fri': 'Friday',
            'Sat': 'Saturday'
        };
        var fix_nameday = dayAliases[day_name];
        var workinghours = [];
        var is_holiday = false;
        var is_closed = false;
        // var tess = '2024-06-03 06:00:00'
        
        // get salon booking time
        function getSalonBookingTime() {
            rpc.query({
                model: 'salon.booking',
                method: 'search_read',
                args: [[]],
                kwargs: {
                    fields: ['id', 'name', 'time', 'chair_id']
                }
            }).then(function(data) {
                data.forEach(record => {
                    // console.log("Data Pemesanan:", record);
                    time_booking.push(record.time);
                });
            }).catch(function (error) {
                console.error("Error:", error);
            });
        }
        
        // get salon holiday 
        function getSalonHoliday() {
            rpc.query({
                model: 'salon.holiday',
                method: 'search_read',
                args: [[]],
                kwargs: {
                    fields: ['id', 'name', 'holiday'],
                }
            }).then(function(data) {
                // Proses data yang diterima dari server
                data.forEach(holy => {
                    // console.log("Data Pemesanan:", holy);
                    if (holy.holiday === true) {
                        salon_holiday.push(holy.name);
                    }
                });
                // Check if the entered day matches a holiday with holiday=true
                if (salon_holiday.includes(fix_nameday)) {
                    alert("The salon is on holiday.");
                    is_holiday = true;
                }
            }).catch((err) => {
                console.log(err)
            })
        }
        
        // get salon working hours
        function getSalonWorkingHours() {
            rpc.query({
                model: 'salon.working.hours',
                method: 'search_read',
                args: [[]],
                kwargs: {
                    fields: ['id', 'name', 'from_time', 'to_time']
                }
            }).then(function(data) {
                data.forEach(workHour => {
                    // console.log("Working Hours:", workHour);
                    if (workHour.name === fix_nameday) {
                        workinghours.push(workHour);
                    }
                });
                // filter
                workinghours.forEach(el=> {
                    var start_time = String(el.from_time).padStart(2, '0') + ":00";
                    var end_time =  String(el.to_time).padStart(2, '0') + ":00";
                    // var fix_time = fix_datetime.substring(11, 19);
                    // console.log('time : ', time);
                    if (time < start_time || time > end_time) {
                        alert("the salon closed.");
                        is_closed = true;
                    }
                });
            });
        }
        // console.log('working hour :', workinghours);

        for (var i = 0; i < (service.length); i++) {
            var k = { i: service[i].attributes['service-id'].value };
            list_service.push(k);
        }

        Promise.allSettled([getSalonBookingTime(), getSalonHoliday(), getSalonWorkingHours()]).then(function() {
            if (name == "" || date == "" || time == "" || phone == "" || email == "" || list_service.length == 0) {
                alert("All fields are mandatory");
            } else if (today < 2) {
                alert("Booking time must be at least 2 hours ahead.");
            } else if (is_closed || is_holiday) {
                alert("Check again date/time booking.");
            } else if (time_booking.includes(fix_datetime)) {
                alert("Time already booked!");
            } else {
                var time_left_char = time.substring(0, 2);
                var time_right_char = time.substring(3, 5);
                var time_separator = time.substring(2, 3);
                if (isNaN(time_left_char) || isNaN(time_right_char) || time_separator != ":") {
                    alert("Select a valid Time");
                } else {
                    var time_left = parseInt(time_left_char);
                    var time_right = parseInt(time_right_char);
                    if ((time_left < 24) && (time_right < 60) && (time_left >= 0) && (time_right >= 0)) {
                        var booking_record = { 'name': name, 'date': date, 'time': time, 'phone': phone, 'email': email, 'list_service': list_service, 'chair': chair, 'number': number };
                        $.ajax({
                            url: "/page/salon_details",
                            type: "POST",
                            dataType: "json",
                            data: booking_record,
                            success: function (data) {
                                window.location.href = "/page/salon_management/salon_booking_thank_you";
                            },
                            error: function (error) {
                                alert('error: ' + error);
                            }
                        });
                    } else {
                        alert("Select a valid time");
                    }
                }
            }
        })
        
    });

    // function getSalonBookingTime() {
    //     return rpc.query({
    //         model: 'salon.booking',
    //         method: 'search_read',
    //         args: [[]],
    //         kwargs: {
    //             fields: ['id', 'name', 'time']
    //         }
    //     });
    // }
    
    // function getSalonHoliday() {
    //     return rpc.query({
    //         model: 'salon.holiday',
    //         method: 'search_read',
    //         args: [[]],
    //         kwargs: {
    //             fields: ['id', 'name', 'holiday'],
    //         }
    //     });
    // }
    
    // function getSalonWorkingHours() {
    //     return rpc.query({
    //         model: 'salon.working.hours',
    //         method: 'search_read',
    //         args: [[]],
    //         kwargs: {
    //             fields: ['id', 'name', 'from_time', 'to_time']
    //         }
    //     });
    // }

    $(document).on('click', "#check_button", function () {
        var check_date = $("#check_date").val();
        if (check_date != "") {
            ajax.jsonRpc("/page/salon_check_date", 'call', {
                'check_date': check_date
            }).then(function (order_details) {
                var x;
                var total_orders = "";
                var order = "";
                var chair_name;
                for (x in order_details) {
                    var chair_name = order_details[x]['name']
                    var i;
                    var lines = "";
                    for (i = 0; i < order_details[x]['orders'].length; i++) {
                        lines += '<tr><td><span>' + order_details[x]['orders'][i]['number'] +
                            '</span></td><td><span>' + order_details[x]['orders'][i]['start_time_only'] +
                            '</span></td><td><span>' + order_details[x]['orders'][i]['end_time_only'] + '</span></td></tr>'
                    }
                    order += '<div class="col-lg-4 s_title pt16 pb16"><div style="height: 200px!important; text-align: center;' +
                        'border: 1px solid #666;padding: 15px 0px;box-shadow: 7px 8px 5px #888888;background-color:#7c7bad;border-radius:58px;color:#fff;margin-bottom: 10px;">' +
                        '<span style="font-size: 15px;">' + chair_name + '</span>' +
                        '<br/><a style="color:#fff;font-size:15px;">Order Details</a>' +
                        '<div id="style-2" style="overflow-y:scroll;height:105px;padding-right:25px;padding-left:25px;margin-right:10px;">' +
                        '<table class="table"><th style="font-size:11px;">Order No.</th><th style="font-size:11px;">Start Time</th>' +
                        '<th style="font-size:11px;">End Time</th><div><tbody style="font-size: 10px;">' +
                        lines + '</tbody></div></table></div></div></div>'
                }
                total_orders += '<div id="booking_chair_div" class="col-lg-12 s_title pt16 pb16 row">' + order + '</div>'
                var res = document.getElementById('booking_chair_div')
                res.innerHTML = "";
                res.innerHTML = total_orders;
                var date_value = 'DATE : <t>' + check_date + '</t>'
                var date_field = document.getElementById('searched_date')
                date_field.innerHTML = "";
                date_field.innerHTML = date_value;
            });
        } else {
            alert("Fill the Field");
        }
    });

});
