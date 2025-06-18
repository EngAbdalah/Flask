from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods = ['GET']) # url
def hello_world(): # view
	return "Hello, Assiut!"


#@app.route('/<str: name>')
#def hello(name):
#	return f'Hello, {name}!'

jobs = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'Cairo',
        'company': 'Tech Company'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Alexandria',
        'company': 'Data Corp'
    },
    {
        'id': 3,
        'title': 'Web Developer',
        'location': 'Zagazig',
        'company': 'Web Solutions'
    },
    {
        'id': 4,
        'title': 'Mobile Developer',
        'location': 'Cairo',
        'company': 'App Innovations'
    },
    {
        'id': 5,
        'title': 'DevOps Engineer',
        'location': 'Giza',
        'company': 'Cloud Services'
    }
]

	
@app.route('/jobs/list', methods = ['GET'])
def list_jobs():
    return render_template('jobs_list.html', jobs = jobs)


"""
Lab:

- create end points for:
    - single job by id
    - create list endpoint for companies (id, name, location, industry, employees count)
    - single company by id

"""



@app.route("/jobs/<int:job_id>")
def get_job_by_id(job_id):
	for j in jobs:
		if j["id"]== job_id:
			return render_template('jobs_by_id.html', job = j)
	return "job id not found ", 404
		
		
		
		
		
companies = [
    {
    "id": 1,
     "name": "TechCorp",
     "location": "Cairo", 
     "industry": "Software", 
     "employees_count": 150
     },
     
    {
    "id": 2, 
    "name": "GreenFields", 
    "location": "Assiut", 
    "industry": "Agriculture", 
    "employees_count": 50
    }
]
@app.route("/companies", methods = ['GET'])
def list_companies():
    return render_template('companies_list.html', companies=companies)
    
@app.route("/company/<int:company_id>")
def get_company_by_id(company_id):
	for c in companies:
		if c["id"]== company_id:
			return render_template('companies_by_id.html', company = c)
	return "job id not found ", 404
		
		

	
