from flask import Flask, render_template, request 
from merge import LinkedList

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/more')
def more():
    return render_template('more.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ppage', methods=['GET', 'POST'])
def ppage():
    return render_template('programPage.html')

@app.route('/upper', methods=['GET', 'POST'])
def upper():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('toUpper.html', result=result)

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    result = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', 0))
            if radius >=0:
                area = 3.14159 * radius**2
                result = f"The area of the circle with the radius of {radius} is {area: .2f}"
            else:
                result = "Radius should be a non-negative number."
        except ValueError:
            result = "Invalid input. Please enter a valid number for radius."

    return render_template('circle.html', result=result)


@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    result = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', 0))
            height = float(request.form.get('height', 0))
            if base >=0 and height >= 0:
                area = 0.5 * base * height
                result = f"The area of the triangle with a base of {base} and height of {height} is {area:.2f} square units."
            else:
                result = "Base and height should be a non-negative number."
        except ValueError:
            result = "Invalid input. Please enter a valid number for base and height."

    return render_template('triangle.html', result=result)



@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/merge", methods=['GET', 'POST'])
def mergeLinkLists():
    result = None
    error = None
    list1 = None
    list2 = None
    mll = LinkedList()

    if request.method == 'POST':
        try:
            array_size1 = int(request.form.get('size1', 0))
            ask_val1 = request.form.get('value1', '')
            value1 = [val.strip() for val in ask_val1.split(',')]
            if array_size1 != len(value1):
                raise ValueError("Size should be equal to the number of values for Linked List 1.")
            list1 = mll.linked_list(array_size1, value1)

            array_size2 = int(request.form.get('size2', 0))
            ask_val2 = request.form.get('value2', '')
            value2 = [val.strip() for val in ask_val2.split(',')]
            if array_size2 != len(value2):
                raise ValueError("Size should be equal to the number of values for Linked List 2.")
            list2 = mll.linked_list(array_size2, value2)

            result = mll.mergeLinkLists(list1, list2)

        except ValueError as e:
            error = str(e)

    return render_template('merge.html', result=result, error=error, print_ll=mll.printLinkedList, list1=list1, list2=list2)



if __name__ == "__main__":
    app.run(debug=True)
