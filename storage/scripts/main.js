"use strict"


async function sendFile(file) {
    let response = await fetch(
        "/render",
        {
            method: "POST",
            headers: {
                "Content-Type": "text/plain",
            },
            body: file
        }
    )

    let image = await response.blob()
    let src = URL.createObjectURL(image)
    $("#graph")[0].src = src

    $("label").hide()
}


let uploadInput = $("#uploadInput")
uploadInput.on("change", () => sendFile(uploadInput[0].files[0]))

let imageViewer = $("#graphContainer")
imageViewer.on("drop", (event) => {
    event.preventDefault()

    console.log(event)

    let data = event.originalEvent.dataTransfer.items

    if (data) {
        if (data[0].kind === "file") {
            sendFile(data[0].getAsFile())
        }
    }

    imageViewer.css("background-color", "#ffffff")
})

imageViewer.on("dragenter", (event) => {
    event.preventDefault()
    imageViewer.css("background-color", "#bcefff")
})

imageViewer.on("dragexit", (event) => {
    event.preventDefault()
    imageViewer.css("background-color", "#ffffff")
})

imageViewer.on("dragover", (event) => event.preventDefault())