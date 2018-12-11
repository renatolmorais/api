#!c:\python27\python.exe
#encoding: UTF-8

def get_element( name,form ):
	if name in form: return form[name].value
	else: return ''
import sys,os
import cgi, cgitb
cgitb.enable()

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
if 'issubmit' in form:
	print get_element( 'corretora',form )
	print get_element( 'value', form )
	print get_element( 'ativo', form )

else: 
	print '''<!DOCTYPE html>
<html>
  <head>
    <base target="_top">
	<style>
     {box-sizing: border-box;}

/* Button used to open the contact form - fixed at the bottom of the page */
.open-button {
  background-color: #555;
  color: white;
  padding: 16px 20px;
  border: none;
  cursor: pointer;
  opacity: 0.8;
  position: fixed;
  bottom: 23px;
  right: 28px;
  width: 280px;
}

/* The popup form - hidden by default */
.form-popup {
  display: visible;
  width: 100%;
  #position: fixed;
  #bottom: 0;
  #right: 15px;
  border: 3px solid #f1f1f1;
  z-index: 9;
}

/* Add styles to the form container */
.form-container {
  width: 100%;
  padding: 1px;
  background-color: white;
}

/* Full-width input fields */
.form-container input[type=text], .form-container input[type=password] {
  width: 60%;
  padding: 5px;
  margin: 5px 0 22px 0;
  border: none;
  background: #f1f1f1;
}

/* When the inputs get focus, do something */
.form-container input[type=text]:focus, .form-container input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}

/* Set a style for the submit/login button */
.form-container .btn {
  background-color: #4CAF50;
  color: white;
  padding: 5px;
  border: none;
  cursor: pointer;
  width: 50%;
  margin-bottom:10px;
  opacity: 0.8;
}

/* Add a red background color to the cancel button */
.form-container .cancel {
  background-color: red;
}

/* Add some hover effects to buttons */
.form-container .btn:hover, .open-button:hover {
  opacity: 1;
} 
    </style>
	</head>
  <body align="center">
     <div class="form-popup" id="myForm">
  <form action="http://localhost:8080/api" class="form-container">
    <label for="email"><b>Corretora</b></label>
    <input type="text" placeholder="Corretora" name="corretora" required><br>
    
    <label for="email"><b>Ativo</b></label>
    <input type="text" placeholder="Ativo" name="ativo" required><br>
    
    <label for="email"><b>Quantidade</b></label>
    <input type="text" placeholder="0" id="idquant" name="quantidade" required><br>
    
    <label for="email"><b>Pre&ccedil;o</b></label>
    <input type="text" placeholder="0.0" id="idprice" name="preco" required><br>
    
    <label for="email"><b>Valor</b></label>
    <input type="text" placeholder="Valor" id="idvalue" name="valor" required><br>
	
	<input type="hidden" name="issubmit" value="true">

    <button type="submit" class="btn">Salvar</button>
  </form>
</div> 

<script src="http://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script>

$(document).ready(function() {

    $("#idquant").change(function() {
        var quant = $("#idquant").val();
        var price = $("#idprice").val();
        $("#idvalue").val(quant * price);
      }
    );
    
    $("#idprice").change(function() {
        var quant = $("#idquant").val();
        var price = $("#idprice").val();
        $("#idvalue").val(quant * price);
      }
    );    
  }
);

</script>
  </body>
</html>'''