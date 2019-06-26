window.onload = function () {
     document.getElementById("eerste").style.display = "block";
     document.getElementById("tweede").style.display = "none";
     document.getElementById("regForm").style.display = "none";
};

document.getElementById("but").onclick = function() {
    document.getElementById("tweede").style.display = "block";
    document.getElementById("regForm").style.display = "block";
    document.getElementById("eerste").style.display = "none";
};

var answers = {};
var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
    // This function will display the specified tab of the form...
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    //... and fix the Previous/Next buttons:
    if (n == 0) {
        document.getElementById("prevBtn").style.display = "none";
    } else {
        document.getElementById("prevBtn").style.display = "inline";
    }
    //... and run a function that will display the correct step indicator:
    fixStepIndicator(n)
}

function nextPrev(n, answer) {
    // This function will figure out which tab to display
    var x = document.getElementsByClassName("tab");
    // Exit the function if any field in the current tab is invalid:
    if (n == 1 && !validateForm()) return false;
    if (answer) {
        answers[currentTab + 1] = answer;
    }
    // Hide the current tab:
    x[currentTab].style.display = "none";
    // Increase or decrease the current tab by 1:
    currentTab = currentTab + n;
    // if you have reached the end of the form...
    if (currentTab >= x.length) {
        // ... the form gets submitted:
        document.getElementById("regForm").submit();
        return false;
    }
    // Otherwise, display the correct tab:
    showTab(currentTab);
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?

            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function results () {
    stad = document.getElementById("stadnaam").innerText;

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    });
    $.ajax({
        url: "/api/uitslag",
        type: "POST",
        data: { stad: stad },
        dataType: "json",
        success: function (result) {
            results2(result);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            alert(xhr.status);
            alert(thrownError);
        }
    });
}

function results2 (result) {
    var score = {}
    for (var i in answers) {
        vergelijk0 = answers[i]
        verant = result[i];
        for (ant in verant) {
            vergelijk1 = verant[ant]
            if (vergelijk0 == vergelijk1) {
                score[ant] = score[ant] + 1 || 1
                console.log(score);
            };
        };
    };
    document.getElementById('tekst').innerHTML = "<p>De volgende verenigingen sluiten het beste aan bij jouw antwoorden op deze kieswijzer:</p>"
    document.getElementById('resultaten').innerHTML = '<ul id="list"></ul>';
    var list = document.getElementById("list")

    var items = Object.keys(score).map(function(key) {
        return [key, score[key]];
    });
    items.sort(function(first, second) {
        return second[1] - first[1];
    });
    var temp = items.slice(0, 5);

    console.log(temp);
    console.log(items);

    for (i in temp) {
        var list_item = document.createElement("li");
        list_item.className = "list-group-item";
        list_item.innerHTML = `${temp[i][0]}: <span class="badge badge-warning"> ${temp[i][1]}/15 </span>`;
        list.appendChild(list_item);
    }
};

function validateForm() {
    // This function deals with validation of the form fields
    var x, y, i, valid = true;
    x = document.getElementsByClassName("tab");
    y = x[currentTab].getElementsByTagName("input");
    // A loop that checks every input field in the current tab:
    for (i = 0; i < y.length; i++) {
        // If a field is empty...
        if (y[i].value == "") {
            // add an "invalid" class to the field:
            y[i].className += " invalid";
            // and set the current valid status to false
            valid = false;
        }
    }
    // If the valid status is true, mark the step as finished and valid:
    if (valid) {
        document.getElementsByClassName("step")[currentTab].className += " finish";
    }
    return valid; // return the valid status
}

function fixStepIndicator(n) {
    // This function removes the "active" class of all steps...
    var i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(" active", "");
    }
    //... and adds the "active" class on the current step:
    x[n].className += " active";
}
