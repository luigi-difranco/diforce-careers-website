// Generate header image with mountains and palm tree
document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('headerCanvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');

    // Set canvas size
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;

    // Colors from Frozen Mist palette
    const colors = {
        grayDark: '#7C7D75',
        grayLight: '#ADACA7',
        cream: '#FCF8D8',
        grayMedium: '#D9DADF',
        cinnamon: '#DD700B'
    };

    // Background
    ctx.fillStyle = colors.cream;
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw mountains
    function drawMountains() {
        // Left mountain
        ctx.beginPath();
        ctx.moveTo(50, canvas.height);
        ctx.lineTo(120, canvas.height * 0.4);
        ctx.lineTo(190, canvas.height);
        ctx.strokeStyle = colors.grayDark;
        ctx.lineWidth = 3;
        ctx.stroke();

        // Mountain shading
        ctx.beginPath();
        ctx.moveTo(50, canvas.height);
        ctx.lineTo(120, canvas.height * 0.4);
        ctx.lineTo(190, canvas.height);
        ctx.closePath();
        ctx.fillStyle = colors.grayLight + '30';
        ctx.fill();

        // Right mountain
        ctx.beginPath();
        ctx.moveTo(150, canvas.height);
        ctx.lineTo(250, canvas.height * 0.5);
        ctx.lineTo(350, canvas.height);
        ctx.strokeStyle = colors.grayDark;
        ctx.lineWidth = 3;
        ctx.stroke();
    }

    // Draw palm tree
    function drawPalmTree() {
        const treeX = canvas.width - 120;
        const treeY = canvas.height - 40;

        // Trunk
        ctx.beginPath();
        ctx.moveTo(treeX, treeY);
        ctx.quadraticCurveTo(treeX + 5, treeY - 30, treeX + 10, treeY - 60);
        ctx.strokeStyle = colors.grayDark;
        ctx.lineWidth = 4;
        ctx.stroke();

        // Palm fronds
        const frondCount = 6;
        const frondLength = 35;

        for (let i = 0; i < frondCount; i++) {
            const angle = (Math.PI * 2 / frondCount) * i - Math.PI / 2;
            const endX = treeX + 10 + Math.cos(angle) * frondLength;
            const endY = treeY - 60 + Math.sin(angle) * frondLength;

            // Main frond line
            ctx.beginPath();
            ctx.moveTo(treeX + 10, treeY - 60);
            ctx.quadraticCurveTo(
                treeX + 10 + Math.cos(angle) * frondLength * 0.6,
                treeY - 60 + Math.sin(angle) * frondLength * 0.6,
                endX,
                endY
            );
            ctx.strokeStyle = colors.grayDark;
            ctx.lineWidth = 3;
            ctx.stroke();

            // Frond details
            const detailCount = 4;
            for (let j = 1; j <= detailCount; j++) {
                const t = j / (detailCount + 1);
                const px = treeX + 10 + Math.cos(angle) * frondLength * t;
                const py = treeY - 60 + Math.sin(angle) * frondLength * t;

                // Left side detail
                const leftAngle = angle - Math.PI / 6;
                ctx.beginPath();
                ctx.moveTo(px, py);
                ctx.lineTo(
                    px + Math.cos(leftAngle) * 8,
                    py + Math.sin(leftAngle) * 8
                );
                ctx.strokeStyle = colors.grayDark;
                ctx.lineWidth = 2;
                ctx.stroke();

                // Right side detail
                const rightAngle = angle + Math.PI / 6;
                ctx.beginPath();
                ctx.moveTo(px, py);
                ctx.lineTo(
                    px + Math.cos(rightAngle) * 8,
                    py + Math.sin(rightAngle) * 8
                );
                ctx.stroke();
            }
        }
    }

    // Draw ground line
    function drawGround() {
        ctx.beginPath();
        ctx.moveTo(0, canvas.height - 20);
        ctx.lineTo(canvas.width, canvas.height - 20);
        ctx.strokeStyle = colors.grayDark;
        ctx.lineWidth = 2;
        ctx.stroke();
    }

    // Draw decorative elements
    function drawDecorations() {
        // Add some subtle accent marks
        ctx.strokeStyle = colors.cinnamon + '40';
        ctx.lineWidth = 2;

        // Small decorative line near title
        ctx.beginPath();
        ctx.moveTo(30, 80);
        ctx.lineTo(80, 80);
        ctx.stroke();
    }

    // Execute drawing
    drawMountains();
    drawPalmTree();
    drawGround();
    drawDecorations();

    // Handle window resize
    let resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
            canvas.width = canvas.offsetWidth;
            canvas.height = canvas.offsetHeight;

            ctx.fillStyle = colors.cream;
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            drawMountains();
            drawPalmTree();
            drawGround();
            drawDecorations();
        }, 250);
    });
});