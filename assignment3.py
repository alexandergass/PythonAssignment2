import cgi;
from wsgiref.simple_server import make_server;
import MySQLdb;
import MySQLdb.cursors;

db = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='root', db='assignment3', cursorclass=MySQLdb.cursors.DictCursor);
cursor = db.cursor( );

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>pyhtml web page</title>
    </head>
    <body>
        <form action="" method="POST">
            <label>Title<br /></label><SELECT name="title"><OPTION VALUE=""></OPTION>
            <OPTION VALUE="Mr">Mr</OPTION>
            <OPTION VALUE="Mrs">Mrs</OPTION>
            <OPTION VALUE="Ms">Ms</OPTION>
            <OPTION VALUE="Dr">Dr</OPTION>
            </SELECT>
            <br />
            
            <label for="name">First Name</label>
            <br />
            <input type="text" name="first" value="" />
            <br />

            <label for="name">Last Name</label>
            <br />
            <input type="text" name="last" value="" />
            <br />

            <label for="name">Street</label>
            <br />
            <input type="text" name="street" value="" />
            <br />

            <label for="name">City</label>
            <br />
            <input type="text" name="city" value="" />
            <br />

            <label for="name">Province</label>
            <br />
            <input type="text" name="province" value="" />
            <br />

            <label for="name">Postal Code</label>
            <br />
            <input type="text" name="postalcode" value="" />
            <br />

            <label>Country<br /></label><SELECT name="country"><OPTION VALUE=""></OPTION>
            <OPTION VALUE="Canada" <?php if ($country=="Canada") echo "selected"; ?>Canada</OPTION>
            <OPTION VALUE="USA" <?php if ($country=="USA") echo "selected"; ?>USA</OPTION>
            </SELECT>
            <br />

            <label for="name">Phone</label>
            <br />
            <input type="text" name="phone" value="" />
            <br />

            <label for="name">Email</label>
            <br />
            <input type="text" name="email" value="" />
            <br />

            <label>News Letter</label><br />
            <input type="checkbox" name="newsletter" value="on" />
            <br />
            
            <br />
            <input type="submit" name="submit" value="Submit" />
        </form>
    </body>
</html>
       """;
    
def app (environ, start_response):
    response = html;
    if ( environ['REQUEST_METHOD'] == "POST"):
        post_env = environ.copy();
        post_env["QUERY_STRING"] = "";

        post = cgi.FieldStorage(
            fp = environ["wsgi.input"],
            environ = post_env,
            keep_blank_values=True
        );

        titleVar = post["title"].value;
        firstVar = post["first"].value;
        lastVar = post["last"].value;
        streetVar = post["street"].value;
        cityVar = post["city"].value;
        provinceVar = post["province"].value;
        postalVar = post["postalcode"].value;
        countryVar = post["country"].value;
        phoneVar = post["phone"].value;
        emailVar = post["email"].value;

        if post.getvalue('newsletter'):
            newsVar = "YES";
        else: 
            newsVar = "NO";
        # print(newsVar);

        e1 = "";
        e2 = "";
        e3 = "";
        e4 = "";
        e5 = "";    
        e6 = ""; 
        e7 = ""; 
        e8 = ""; 
        e9 = ""; 
        e10 = "";     

        # print(titleVar);

        if (titleVar==""):
            errors = 1;
            e1 = "<span style='color: red'>*required</span>";
        if (firstVar==""):
            errors = 1;
            e2 = "<span style='color: red'>*required</span>";
        if (lastVar==""):
            errors = 1;
            e3 = "<span style='color: red'>*required</span>";
        if (streetVar==""):
            errors = 1;
            e4 = "<span style='color: red'>*required</span>";
        if (cityVar==""):
            errors = 1;
            e5 = "<span style='color: red'>*required</span>";
        if (provinceVar==""):
            errors = 1;
            e6 = "<span style='color: red'>*required</span>";
        if (postalVar==""):
            errors = 1;
            e7 = "<span style='color: red'>*required</span>";
        if (countryVar==""):
            errors = 1;
            e8 = "<span style='color: red'>*required</span>";
        if (phoneVar==""):
            errors = 1;
            e9 = "<span style='color: red'>*required</span>";
        if (emailVar==""):
            errors = 1;
            e10 = "<span style='color: red'>*required</span>";
        elif (titleVar!="" and firstVar!="" and lastVar!="" and streetVar!="" and cityVar!="" and provinceVar!="" and postalVar!="" and countryVar!="" and phoneVar!="" and emailVar!=""):
            errors = 0;

        if (errors != 0):
            response2 = """
            <!DOCTYPE html>
            <html>
                <head>
                    <title>pyhtml web page</title>
                </head>
                <body>
                    <form action="" method="POST">

                        <label>Title<br /></label>
                        <SELECT name="title"><OPTION VALUE="%s">%s</OPTION>
                        <OPTION VALUE="Mr">Mr</OPTION>
                        <OPTION VALUE="Mrs">Mrs</OPTION>
                        <OPTION VALUE="Ms">Ms</OPTION>
                        <OPTION VALUE="Dr">Dr</OPTION>
                        </SELECT>%s
                        <br />
                        
                        <label for="name">First Name</label>
                        <br />
                        <input type="text" name="first" value="%s" />%s
                        <br />

                        <label for="name">Last Name</label>
                        <br />
                        <input type="text" name="last" value="%s" />%s
                        <br />

                        <label for="name">Street</label>
                        <br />
                        <input type="text" name="street" value="%s" />%s
                        <br />

                        <label for="name">City</label>
                        <br />
                        <input type="text" name="city" value="%s" />%s
                        <br />

                        <label for="name">Province</label>
                        <br />
                        <input type="text" name="province" value="%s" />%s
                        <br />

                        <label for="name">Postal Code</label>
                        <br />
                        <input type="text" name="postalcode" value="%s" />%s
                        <br />

                        <label>Country<br /></label>
                        <SELECT name="country"><OPTION VALUE="%s">%s</OPTION>
                        <OPTION VALUE="Canada" <?php if ($country=="Canada") echo "selected"; ?>Canada</OPTION>
                        <OPTION VALUE="USA" <?php if ($country=="USA") echo "selected"; ?>USA</OPTION>
                        </SELECT>%s
                        <br />

                        <label for="name">Phone</label>
                        <br />
                        <input type="text" name="phone" value="%s" />%s
                        <br />

                        <label for="name">Email</label>
                        <br />
                        <input type="text" name="email" value="%s" />%s
                        <br />

                        <label>News Letter</label><br />
                        <input type="checkbox" name="newsletter" value="%s" />
                        <br />

                        <br />
                        <input type="submit" name="submit" value="Submit" />

                    </form>
                </body>
            </html>
                """;
            response = response2 % (titleVar, titleVar, e1, firstVar, e2, lastVar, e3, streetVar, e4, cityVar, e5, provinceVar, e6, postalVar, e7, countryVar, countryVar, e8, phoneVar, e9, emailVar, e10, newsVar);
        else:    
            sql = """INSERT INTO registered_users (
                    title, firstname, lastname, street, city, province, postalcode, country, phone, email, newsletter)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""";
            values = (titleVar, firstVar, lastVar, streetVar, cityVar, provinceVar, postalVar, countryVar, phoneVar, emailVar, newsVar);

            cursor.execute(sql, values);
            db.commit();

            cursor.execute("SELECT * FROM registered_users");
            data = cursor.fetchall();
            # print(data);

            response = """<table border="1" cellspacing="2">
                    <tr>
                        <th>user_id</th>
                        <th>Title</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Street</th>
                        <th>City</th>
                        <th>Province</th>
                        <th>Postal Code</th>
                        <th>Country</th>
                        <th>Phone</th>
                        <th>Email</th>
                        <th>Newsletter</th>
                    </tr>
            """;

            # print("Total number of rows is: ", cursor.rowcount);
            # print("");

            for row in data:
                id = row["user_id"];
                newsLetter = row["newsletter"];
                
                response2 = """
                    <tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                    </tr>
                        """;
                response += response2 % (id, titleVar, firstVar, lastVar, streetVar, cityVar, provinceVar, postalVar, countryVar, phoneVar, emailVar, newsLetter);

    start_response('200 OK', [('Content-Type','text/html')]);
    return [response.encode( )];

    cursor.close();
    db.close();

    import gc;
    gc.collect();

if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server;
        httpd = make_server('', 8080, app);
        print('Serving on port 8080...');
        httpd.serve_forever();
    except KeyboardInterrupt:
        print("Goodbye");