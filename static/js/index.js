// function myFunction() {
//     var copyText = document.getElementById("myInput");
//     copyText.outerHTML;
//     copyText.select();
//     copyText.setSelectionRange(0, 99999)
//     document.execCommand("copy");
//     alert("Copied the text: " + copyText.outerHTML);
//   }



// var copyText = document.getElementById("myInput");
// copyText.value = document.getElementById("myTestELement").outerHTML;
// copyText.select();
// copyText.setSelectionRange(0, 99999)
// document.execCommand("copy");

function myFunction() {
var copyText = document.getElementById("myInput");
copyText.value = document.getElementById("myTestELement").outerHTML;
copyText.select();
copyText.setSelectionRange(0, 99999)
document.execCommand("copy");
    alert("Copied the text: " + copyText.outerHTML);
  }


//   function myFunction() {
//     var x = document.getElementsByTagName("h1")[0];
//     x.outerHTML = "<h3>You changed the entire header element and it's content!</h3>";

// function copyText(e) {
//     var textToCopy = document.querySelector(e);
//     var textBox = document.querySelector(".clipboard");
//     textBox.setAttribute('value', textToCopy.outerHTML);

//     textBox.select();
//     document.execCommand('copy');
//   }



  (function() {
    var elements = document.querySelectorAll('[data-tw-bind]'),
        scope = {};
    elements.forEach(function(element) {
        //execute scope setter
        if(element.type === 'text'|| element.type === 'textarea' || element.type === 'button'){
            var propToBind = element.getAttribute('data-tw-bind');
            addScopeProp(propToBind);
            element.onkeyup = function(){
                scope[propToBind] = element.value;
            }
        };

        //bind prop to elements
        function addScopeProp(prop){
            //add property if needed
            if(!scope.hasOwnProperty(prop)){
                //value to populate with newvalue
                var value;
                Object.defineProperty(scope, prop, {
                    set: function (newValue) {
                        value = newValue;
                        elements.forEach(function(element){
                            //change value to binded elements
                            if(element.getAttribute('data-tw-bind') === prop){
                                if(element.type && (element.type === 'text' ||
                                    element.type === 'textarea' || element.type === 'button')){
                                    element.value = newValue;
                                }
                                else if(!element.type){
                                    element.innerHTML = newValue;
                                }
                            }
                        });
                    },
                    get: function(){
                        return value;
                    },
                    enumerable: true
                });
            }
        }
    });

    log = function() {
        Object.keys(scope).forEach(function(key){
            console.log(key + ': ' + scope[key]);
        });
    }

    changeNameByCode = function() {
        scope.name = 'name Changed by Code';
    }

    changeSurnameByCode = function() {
        scope.surname = 'surname Changed by Code';
    }
})();


// function for color picker

// $(document).ready(function(){
//     $('#color-input').change(function(){
//      var color = $(this).val();
//      $('.color-code').html(color);
//      $('.color').css({'background':color})
//    })
//   })


var colorButton = document.getElementById("primary_color");
    var colorDiv = document.getElementById("color_val");
    colorButton.onchange = function() {
        colorDiv.innerHTML = colorButton.value;
        colorDiv.style.color = colorButton.value;
    }
