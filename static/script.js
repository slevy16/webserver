function changePage1() {
  document.location.href = '/';
}
function changePage2() {
  document.location.href = '/feed';
}
function changePage3() {
  document.location.href = '/uploads';
}
function login(username) {
  var x ="username=" + username;
  document.cookie=x;
  changePage2();
}

function checkuserstatus(){
  var x = document.cookie;
  if(x.indexOf('username=') == -1) document.location.href = '/notloggedin';
}
