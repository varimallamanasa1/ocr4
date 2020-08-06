$('#GFG_UP').text("Choose file from system to get the fileSize"); 
$('#File').on('change', function() { 
    if (this.files[0].size > 2097152) { 
        alert("Try to upload file less than 2MB!"); 
    } else { 
         $('#GFG_DOWN').text(this.files[0].name); 
            } 
 }); 
    
