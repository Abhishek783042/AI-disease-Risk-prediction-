const form = document.getElementById("predictionForm");

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    // Get values from form
    const data = {

        pregnancies: Number(
            document.getElementById("pregnancies").value
        ),

        glucose: Number(
            document.getElementById("glucose").value
        ),

        bloodPressure: Number(
            document.getElementById("bloodPressure").value
        ),

        skinThickness: Number(
            document.getElementById("skinThickness").value
        ),

        insulin: Number(
            document.getElementById("insulin").value
        ),

        bmi: Number(
            document.getElementById("bmi").value
        ),

        diabetesPedigreeFunction: Number(
            document.getElementById("diabetesPedigreeFunction").value
        ),

        age: Number(
            document.getElementById("age").value
        )
    };


    try {

        // Send data to FastAPI
        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(data)
            }
        );


        if (!response.ok) {
            throw new Error("Server error");
        }


        // Get response
        const result = await response.json();


        // Display result
        document.getElementById("resultText").textContent =
            result.result;

        document.getElementById("riskScore").textContent =
            "Risk Score: " + result.risk_percentage + "%";


    } catch (error) {

        document.getElementById("resultText").textContent =
            "Unable to connect to the backend.";

        document.getElementById("riskScore").textContent =
            "Please make sure FastAPI is running.";

        console.error(error);
    }

});