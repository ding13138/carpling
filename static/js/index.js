document.addEventListener("DOMContentLoaded", function() {
    // 选取所有 .image-item
    document.querySelectorAll(".image-item").forEach(function(item) {
        item.addEventListener("click", function() {
            let carType = this.getAttribute("data-car"); // 取得车型名称
            window.location.href = `/search?type=${encodeURIComponent(carType)}`; // 跳转到新页面
        });
    });
});
