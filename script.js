document.getElementById("downloadBtn").addEventListener("click", () => {
    const link = document.createElement("a");
    link.href = "http://displayerappp.wuaze.com/release/installer.zip"; // Замените на путь к вашему файлу
    link.download = "installer.zip"; // Имя файла при скачивании
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
});
