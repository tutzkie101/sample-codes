function validateString(strSource)
{
  var strSet;
  var strSetLen;
  var strLen;
  var str = new String(strSource);
	str = str.replace(/(\r\n|\n|\r)/g,' ');
	str = str.replace(/\s+/g,' ');
    
  strLen = str.length;  
  strSet = str.split(" ");
  strSetLen = strSet.length;
  
  /*document.getElementById("outputField").innerHTML = "";*/
  for(var idx = 0;idx<strSetLen;idx++)
  {
	  if(validate(strSet[idx]))
	  {
	    document.getElementById("outputField").innerHTML += strSet[idx] +" VALID<br />";
	  }else
	  {
		document.getElementById("outputField").innerHTML += strSet[idx] +" INVALID<br />";
	  }
  }
}

function validate(str)
{
	
  var bool;
  
  var pattA = /[a-j]/;//1 char
  var pattB = /Z+[a-j]/; //2 chars w/Z
  var pattC = /[NLQR]+[a-j]+[a-j]/; //3 chars
  var pattD = /[NLQR]+Z+[a-j]+[a-j]/; //4 chars w/Z  
	
    switch(str.length)
    {
      case 1:  bool = pattA.test(str);
	    break;
	
      case 2:  bool = pattB.test(str);
	    break;
		
      case 3:  bool = pattC.test(str);
	    break;
		
      case 4:  bool = pattD.test(str);
	    break;
	  
	  default: bool = false;
    }		
	
    return bool;
}