document.getElementById("predictionForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    // Collect form data
    const data = {
        Age: parseInt(document.getElementById("Age").value),
        BusinessTravel: document.getElementById("BusinessTravel").value,
        Department: document.getElementById("Department").value,
        DistanceFromHome: parseInt(document.getElementById("DistanceFromHome").value),
        EnvironmentSatisfaction: parseInt(document.getElementById("EnvironmentSatisfaction").value),
        JobSatisfaction: parseInt(document.getElementById("JobSatisfaction").value),
        MaritalStatus: document.getElementById("MaritalStatus").value,
        MonthlyIncome: parseInt(document.getElementById("MonthlyIncome").value),
        OverTime: document.getElementById("OverTime").value,
        WorkLifeBalance: parseInt(document.getElementById("WorkLifeBalance").value),
        YearsAtCompany: parseInt(document.getElementById("YearsAtCompany").value),
        YearsSinceLastPromotion: parseInt(document.getElementById("YearsSinceLastPromotion").value)
    };

    const submitBtn = event.target.querySelector("button[type='submit']");
    const resultBox = document.getElementById("result");

    submitBtn.disabled = true;
    submitBtn.textContent = "Predicting…";
    resultBox.className = "";
    resultBox.innerHTML = `<p class="loading">Running the model…</p>`;

    try {
        const response = await fetch("https://ibm-hr-backend.onrender.com/api/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.detail || "Something went wrong");
        }

        resultBox.className = "";
        resultBox.innerHTML = `
            <p><strong>Prediction:</strong> ${result.prediction}</p>
            <p><strong>Confidence:</strong> ${result.confidence_score.toFixed(2)}</p>
        `;

        function cleanFeatureName(name) {
            return name
                .replace(/^(nom__|cont__|ord__)/, "")
                .replace(/_(Yes|No)$/i, "")
                .replace(/_/g, " ")
                .trim();
        }

        if (result.top_contributors) {
            let shapHtml = `<h3>Primary Influencing Factors</h3><ul>`;

            result.top_contributors.forEach(item => {
                const cleanName = cleanFeatureName(item.feature);
                const isPositive = item.impact > 0;

                const badgeClass = isPositive ? "impact-up" : "impact-down";
                const indicator = isPositive ? "↑ Contributes to Risk" : "↓ Supports Retention";

                shapHtml += `
                    <li>
                        <div class="factor-info">
                            <span class="factor-name">${cleanName}</span>
                            <span class="factor-badge ${badgeClass}">${indicator}</span>
                        </div>
                    </li>
                `;
            });

            shapHtml += `</ul>`;
            resultBox.innerHTML += shapHtml;
        }

    } catch (error) {
        resultBox.className = "risk-error";
        resultBox.innerHTML = `
            <p style="color:red;">Error: ${error.message}</p>
        `;
    } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = "Run prediction";
    }
});