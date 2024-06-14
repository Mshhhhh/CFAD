document.addEventListener("DOMContentLoaded", function() {
    const username = localStorage.getItem('username')

    document.getElementById("greeting").innerText = `도수는 어느정도가 좋나요?`;
    document.getElementById("nameForm").style.display = 'none';
    document.getElementById("emojiSelection").style.display = 'block';
    document.getElementById("selectedEmoji").innerText = "⚪"; // Reset to default emoji
    const photo = document.getElementById("predefinedPhoto");
    if (photo) {
        photo.style.display = 'none';
    }


});


function selectEmoji(emojiId, value, text) {
    const emojis = {
        emoji1: "🍹",
        emoji2: "🍸",
        emoji3: "🍾️",
        emoji4: "🤷‍♂️"
    };
    document.getElementById("selectedEmoji").innerText = emojis[emojiId];
    document.getElementById("displayName").innerText = text;
    sessionStorage.setItem('alcoholvalue', value);
}
