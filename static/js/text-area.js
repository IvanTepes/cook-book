 /* Create two constant for each text-area */
    const ingredients = document.getElementById('recipe_ingredients');
    const method = document.getElementById('recipe_method');


    /* On focus out check if user try submit empty form
        if so disable button and display modal message.
        Try to override materialize valid form after 5 blank spaces
        Materialize validation display valid form if user try send empty 
        form
    */
    ingredients.addEventListener('focusout', (event) => {
        if (!$.trim($("#recipe_ingredients").val())) {
            // textarea is empty or contains only white-space
            if (ingredients.classList.contains('valid')) {
                // Has valid class in it
                ingredients.classList.remove('valid')
                ingredients.classList.add('invalid')
                document.getElementById('add_button').disabled = true;
                // Has invalid class in it
                if (ingredients.classList.contains('invalid')) {
                    $('#empty_modal').modal();
                    $('#empty_modal').modal('open'); 
                }            
            } else {
                document.getElementById('add_button').disabled = false;
            }
        }
    });
    
    
    method.addEventListener('focusout', (event) => {
        if (!$.trim($("#recipe_method").val())) {
            // textarea is empty or contains only white-space
            if (method.classList.contains('valid')) {
                // Has valid class in it
                method.classList.remove('valid')
                method.classList.add('invalid')
                document.getElementById('add_button').disabled = true;
                // Has invalid class in it
                if (method.classList.contains('invalid')) {
                    $('#empty_modal').modal();
                    $('#empty_modal').modal('open'); 
                }            
            } else {
                document.getElementById('add_button').disabled = false;
            }
        }
    });

    /* Created this event lisener after user try submit empty form, if he 
    delete empty spaces submit button is not show this lisener fix that*/

    /* On focus out check if both method and ingredients have class valid 
    if so display button */
    method.addEventListener('focusout', (event) => {
        if (method.classList.contains('valid')) {
            // Display Button
            document.getElementById('add_button').disabled = false;
        }
    });

    ingredients.addEventListener('focusout', (event) => {
        if (ingredients.classList.contains('valid')){
            // Display Button
            document.getElementById('add_button').disabled = false;
        }
    });
