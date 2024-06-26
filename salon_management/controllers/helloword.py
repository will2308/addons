from odoo import http
# from odoo.http import request

class HelloWorld(http.Controller):
    @http.route('/helloworld', type="http", auth="public", website=True)
    def hello_world(self):
        # # Render navbar from navbar.xml
        # navbar = http.request.env.ref('salon_management.website_navbar')
        # navbar_content = navbar_template.render({})
        # print('*******************************', navbar_template)
        
        # Combine navbar and main content
        output = f"""
            <html>
                <head>
                    <title>Hello World</title>
                    <link href="/salon_management/static/src/css/bootstrap.min.css" rel="stylesheet">
                </head>
                <body>
                    <div class="container" id="helloworld">
                        <nav class="navbar navbar-expand-lg navbar-light bg-light">
                            <a class="navbar-brand" href="#">Navbar</a>
                            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                            </button>
                            <div class="collapse navbar-collapse" id="navbarNav">
                            <ul class="navbar-nav">
                                <li class="nav-item active">
                                <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="#">Features</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="#">Pricing</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
                                </li>
                            </ul>
                            </div>
                        </nav>
                                            
                        <!-- Main content -->
                        <div class="jumbotron">
                            <h1 class="display-4">Hello, world!</h1>
                            <p class="lead">This is a simple hero unit, a simple jumbotron-style component for calling extra attention to featured content or information.</p>
                            <hr class="my-4">
                            <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
                            <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
                        </div>
                    </div>
                </body>
            </html>
        """
        return output