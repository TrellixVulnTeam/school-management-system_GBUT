var baseurl = 'http://127.0.0.1:8000/';
var second = 'http://127.0.0.1:8000/administrator/create';

var token = document.getElementById('myToken').value;

var current_session_pk = 0;
var current_student_pk = 0;


function updaterResult(pk){
	var url = "http://127.0.0.1:8000/administrator/add_student_result/" + pk +"/"; 

	var myForm = new FormData();

	myForm.append('first_test',document.getElementById('first_test_'+pk).value);
	myForm.append('second_test',document.getElementById('second_test_'+pk).value);
	myForm.append('exam',document.getElementById('exam_'+pk).value);

	var xhr = new XMLHttpRequest();
	
	xhr.onload = function(){
         
         console.log('done processing');
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



function CollectCelebrity(name){
	var url = baseurl + 'administrator/kg1/' + name

	console.log(url);
	var xhr = new XMLHttpRequest();

	xhr.onload = function(){
		if(xhr.status == 200){
			response = JSON.parse(xhr.responseText);
			console.log(response);
			var description = response['detail'];
			console.log(description);
			document.getElementById('detail').textContent = response['detail'];
			document.getElementById('session').textContent = response['session'];

			current_student_pk = response['user_id'];
			// document.getElementById('test').textContent = response['first_test'];
			// document.getElementById('first').textContent = response['form'];

		}
	}

xhr.open('GET', url, true);
xhr.send();

}

function Close(){
	document.getElementById('test').style.display = 'none';
}