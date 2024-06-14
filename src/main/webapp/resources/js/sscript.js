document.addEventListener("DOMContentLoaded", function() {
    const username = localStorage.getItem('username')

    document.getElementById("greeting").innerText = `${username}님, 오늘 기분 어때요?`;
    document.getElementById("displayName").innerText = username;
    document.getElementById("nameForm").style.display = 'none';
    document.getElementById("emojiSelection").style.display = 'block';
    document.getElementById("selectedEmoji").innerText = "⚪"; // Reset to default emoji
    const photo = document.getElementById("predefinedPhoto");
    if (photo) {
        photo.style.display = 'none';
    }
});
function selectEmoji(emojiId) {
    const emojis = {
        emoji1: "😍",
        emoji2: "😎",
        emoji3: "🧙‍♂️",
        emoji4: "😈",
        emoji5: "😡",
        emoji6: "😐",
        emoji7: "😊",
        emoji8: "💀"
    };

    document.getElementById("selectedEmoji").innerText = emojis[emojiId];
}
