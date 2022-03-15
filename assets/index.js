function navtoggler(){
    let btn =document.getElementById('togglebtn');
    let sidebar =document.getElementById('sidebar');
    if (sidebar.style.display === 'none') {
        sidebar.style.display = 'block';
      } else {
        sidebar.style.display = 'none';
      }
    // sidebar.style.display ='block';
    
    }