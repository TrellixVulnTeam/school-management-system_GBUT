var baseurl = 'http://127.0.0.1:8000/';
var second = 'http://127.0.0.1:8000/administrator/create';
var addresult = 'http://127.0.0.1:8000/administrator/register/';
var token = document.getElementById('myToken').value;

var current_session_pk = 0;
var current_student_pk = 0;


function updaterResult(pk){
	var url = "http://127.0.0.1:8000/administrator/add_student_result/" + pk +"/"; 

	var myForm = new FormData();

	myForm.append('first_test',document.getElementById('first_test_'+pk).value);
	myForm.append('second_test',document.getElementById('second_test_'+pk).value);
	myForm.append('exam',document.getElementById('exam_'+pk).value);

	document.getElementById('data_loading').style.display = "block";

	document.getElementById('loading_save').style.display = "none";

	var xhr = new XMLHttpRequest();
	
	xhr.onload = function(){

		if(xhr.status == 200){

			response = JSON.parse(xhr.responseText);

			var grade = response['grade'];

			var average_new = response['average_new'];

			document.getElementById('average_'+pk).textContent = average_new;

			document.getElementById('grade_'+pk).textContent = grade;


			document.getElementById('loading_save').style.display = "block";

			document.getElementById('data_loading').style.display = "none";

			document.getElementById('button_'+ pk).style.display = "none";
	         
	         console.log('done processing');
	         console.log(response);
	    }
	}

	xhr.open('POST',url,true);
	xhr.setRequestHeader('X-CSRFTOKEN',token)
	xhr.send(myForm);
}

function InputChange(id, self){

	if ( document.getElementById(self).value != "" ){

	    document.getElementById('button_'+id).style.display = "block";
	}

}




function RegisterStudent(){
	var url = 'http://127.0.0.1:8000/administrator/register/';

	var myForm = new FormData();

	myForm.append('surname',document.getElementById('id_surname').value);
	myForm.append('first_name',document.getElementById('id_first_name').value);
	myForm.append('middle_name',document.getElementById('id_middle_name').value);

	myForm.append('date_of_birth',document.getElementById('id_date_of_birth').value);
	myForm.append('email',document.getElementById('id_email').value);
	myForm.append('Registration_Number',document.getElementById('id_Registration_Number').value);

	myForm.append('Phone',document.getElementById('id_Phone').value);
	myForm.append('Address',document.getElementById('id_Address').value);
	myForm.append('Gender',document.getElementById('id_Gender').value);

	myForm.append('current_class',document.getElementById('id_current_class').value);
	myForm.append('current_session',document.getElementById('id_current_session').value);
	myForm.append('current_term',document.getElementById('id_current_term').value);

	document.getElementById('data_loading').style.display = "block";

	document.getElementById('loading_save').style.display = "none";

	var xhr = new XMLHttpRequest();
	
	xhr.onload = function(){

		if(xhr.status == 200){

			response = JSON.parse(xhr.responseText);

			// var grade = response['grade'];

			var saved = response['saved'];

			// document.getElementById('average_'+pk).textContent = average_new;

			// document.getElementById('grade_'+pk).textContent = grade;


			document.getElementById('loading_save').style.display = "block";

			document.getElementById('data_loading').style.display = "none";

			document.getElementById('button_'+ pk).style.display = "none";
			alert(saved)
	         
	         console.log(saved);
	         console.log(response);
	    }
	}

	xhr.open('POST',url,true);
	xhr.setRequestHeader('X-CSRFTOKEN',token)
	xhr.send(myForm);
}

function InputChange(id, self){

	if ( document.getElementById(self).value != "" ){

	    document.getElementById('button_'+id).style.display = "block";
	}

}





function Collect(){
	var url = second;

	ourform = new FormData();

	var first_test = document.getElementById("id_first_test").value;
	var second_test = document.getElementById("id_second_test").value;
	var exam = document.getElementById("id_exam").value;


	ourform.append('FirstTest',first_test);
	ourform.append('SecondTest',second_test);
	ourform.append('Exam',exam);
	// ourform.append('session_id',current_session_pk);
	ourform.append('student_id',current_student_pk);

	console.log('studet' +current_student_pk);


	console.log(url);
	var xhr = new XMLHttpRequest();

	xhr.onload = function(){
		if(xhr.status == 200){
			response = JSON.parse(xhr.responseText);
			console.log(response);
			var description = response['first'];
			var test = response['first_test'];
			var second_test = response['second_test'];
			var exam = response['exam'];

			console.log(description);
			alert(test)
			document.getElementById('test').textContent = response['first_test'];


		}
	}



console.log(token);

xhr.open('POST', url, true);
xhr.setRequestHeader("X-CSRFTOKEN",token);
xhr.send(ourform);

}


