
function validateMatchID() {
    const input = document.getElementById('ID').value.trim();
    const parts = input.split('/');
    const filtered = parts.filter(Boolean);
    const errorMsg = document.getElementById('error-message');
    if (filtered.length !== 6) {
        errorMsg.textContent = "Broken link: Incorrect number of segments.";
        errorMsg.style.color = "red";
        return false;
    }
    // Get the last segment (after the 5th '/')
    const matchID = filtered[5];
    errorMsg.textContent = "Processing data: " + matchID;
    errorMsg.style.color = "green";
    document.getElementById('ID').value = matchID;
    // Keep the message visible longer (reset after 3 seconds)
    setTimeout(() => {
        errorMsg.textContent = "";
    }, 3000);
    return true;
}