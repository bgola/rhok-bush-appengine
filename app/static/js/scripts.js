var d = document;

function validate_form_register() {
	var txtNome = d.getElementById('txtNome').value;
	var txtEmail = d.getElementById('txtEmail').value;
	var txtDDD = d.getElementById('txtDDD').value;
	var txtTelefone = d.getElementById('txtTelefone').value;
	
	if (txtNome == "" || txtEmail == "" || txtDDD == "" || txtTelefone == "") {
		d.getElementById('warning').style.visibility = "visible";
		d.getElementById('warning').innerHTML = "Favor preencher todos os campos!";

	}
	else {
		d.getElementById('formCadastro').submit();
		d.getElementById('warning').style.visibility = "hidden";
	}
}