
document.addEventListener("DOMContentLoaded", function () {
    let avatar = document.getElementById("userAvatar");
    let dropdown = document.getElementById("dropdownMenu");

    // 点击头像时，显示/隐藏菜单
    avatar.addEventListener("click", function (event) {
        dropdown.style.display = (dropdown.style.display === "block") ? "none" : "block";
        event.stopPropagation(); // 阻止事件冒泡，防止点击外部时立即隐藏
    });

    // 点击其他地方时隐藏菜单
    document.addEventListener("click", function (event) {
        if (!avatar.contains(event.target) && !dropdown.contains(event.target)) {
            dropdown.style.display = "none";
        }
    });
});
