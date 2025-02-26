document.addEventListener("DOMContentLoaded", function () {
    const carImages = document.querySelectorAll(".car_img");

    carImages.forEach((img) => {
        let targetPosition = 50; // 目标位置（居中）
        let currentPosition = 50; // 当前实际位置
        let animationFrame;
        let isHovered = false;

        function updatePosition() {
            if (!isHovered) return;

            // 线性插值 (Lerp) 平滑移动
            currentPosition += (targetPosition - currentPosition) * 0.1;
            img.style.objectPosition = `${currentPosition}% center`;

            if (Math.abs(targetPosition - currentPosition) > 0.1) {
                animationFrame = requestAnimationFrame(updatePosition);
            } else {
                cancelAnimationFrame(animationFrame);
            }
        }

        img.addEventListener("mousemove", function (event) {
            const rect = img.getBoundingClientRect();
            const mouseX = event.clientX - rect.left;
            const percentX = (mouseX / rect.width - 0.5) * 2;
            targetPosition = 50 + percentX * 30; // 加大左右移动范围（30%）

            isHovered = true;
            cancelAnimationFrame(animationFrame);
            animationFrame = requestAnimationFrame(updatePosition);
        });

        img.addEventListener("mouseleave", function () {
            targetPosition = 50;
            isHovered = false;
            img.style.transform = "scale(1)"; // 恢复原始大小
            cancelAnimationFrame(animationFrame);
            animationFrame = requestAnimationFrame(updatePosition);
        });

        img.addEventListener("mouseenter", function () {
            img.style.transform = "scale(1.5)"; // 鼠标进入时放大 2 倍
        });
    });
});
