$('#chooseFile').bind('change', function () {
    var filename = $("#chooseFile").val();
    if (/^\s*$/.test(filename)) {
      $(".file-upload").removeClass('active');
      $("#noFile").text("No file chosen..."); 
    }
    else {
      $(".file-upload").addClass('active');
      $("#noFile").text(filename.replace("C:\\fakepath\\", "")); 
    }
  });

  const input = document.getElementById("chooseFile");
  const textArea = document.getElementById("textArea_contract");
  const convertBase64 = (file) => {
    return new Promise((resolve, reject) => {
        const fileReader = new FileReader();
        fileReader.readAsDataURL(file);

        fileReader.onload = () => {
            resolve(fileReader.result);
        };

        fileReader.onerror = (error) => {
            reject(error);
        };
    });
  };

  const uploadFile = async (event) => {
    const file = event.target.files[0];
    const base64 = await convertBase64(file);
    textArea.innerHTML = base64;
  };

  input.addEventListener("change", (e) => {
    uploadFile(e);
  });