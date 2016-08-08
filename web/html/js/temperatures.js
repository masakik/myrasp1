piscinaSelector = [
    {
        color: "lightgrey",
        lo: 0,
        hi: 15
    },
    {
        color: "cyan",
        lo: 15,
        hi: 22
    },
    {
        color: "#00FF00", //green
        lo: 22,
        hi: 30
    },
    {
        color: "yellow",
        lo: 30,
        hi: 35
    },
    {
        color: "red",
        lo: 35,
        hi: 60
    }];

boilerSelector = [
    {
        color: "lightgrey",
        lo: 0,
        hi: 25
    },
    {
        color: "cyan",
        lo: 25,
        hi: 35
    },
    {
        color: "#00FF00", //green
        lo: 35,
        hi: 48
    },
    {
        color: "yellow",
        lo: 48,
        hi: 55
    },
    {
        color: "red",
        lo: 55,
        hi: 60
    }];

roomSelector = [
    {
        color: "lightgrey",
        lo: 0,
        hi: 10
    },
    {
        color: "cyan",
        lo: 10,
        hi: 20
    },
    {
        color: "#00FF00", //green
        lo: 20,
        hi: 25
    },
    {
        color: "yellow",
        lo: 25,
        hi: 32
    },
    {
        color: "red",
        lo: 32,
        hi: 50
    }];
var gg1, gg2, gg3, gg4;
var tempEnvironmentDefaults = {
    value: 0,
    decimals: 1,
    //gaugeWidthScale: 1,
    symbol: '℃',
    pointer: true,
    pointerOptions: {
        toplength: -12,
        bottomlength: 8,
        bottomwidth: 8,
        color: '#8e8e93',
        stroke: '#ffffff',
        stroke_width: 3,
        stroke_linecap: 'round'
    },
    customSectors: roomSelector,
    //hideMinMax: true,
    counter: true,
    startAnimationTime: 2000,
    startAnimationType: ">",
    refreshAnimationTime: 1000,
    refreshAnimationType: "bounce"
}

document.addEventListener("DOMContentLoaded", function (event) {
    gg1 = new JustGage({
        title: "Pool",
        id: "gg1",
        value: 0,
        min: 0,
        max: 60,
        decimals: 1,
        //gaugeWidthScale: 1,
        symbol: '℃',
        pointer: true,
        pointerOptions: {
            toplength: -15,
            bottomlength: 10,
            bottomwidth: 12,
            color: '#8e8e93',
            stroke: '#ffffff',
            stroke_width: 3,
            stroke_linecap: 'round'
        },
        customSectors: piscinaSelector,
        hideMinMax: true,
        counter: true
    });


    gg2 = new JustGage({
        title: $('#gg2').attr('label'),
        id: "gg2",
        min: 0,
        max: 50,
        defaults: tempEnvironmentDefaults
    });

    gg3 = new JustGage({
        title: $('#gg3').attr('label'),
        id: "gg3",
        min: 0,
        max: 50,
        defaults: tempEnvironmentDefaults
    });

    gg4 = new JustGage({
        title: $('#gg4').attr('label'),
        id: "gg4",
        min: 00,
        max: 50,
        defaults: tempEnvironmentDefaults
    });

    document.getElementById('gg1_refresh').addEventListener('click', function () {
        gg1.refresh(getRandomInt(0, 40));
        gg2.refresh(getRandomInt(0, 60));
        gg3.refresh(getRandomInt(10, 35));
        gg4.refresh(getRandomInt(10, 35));
    });


});
function getData() {
    $.getJSON("/api/combined", function (data) {
        //$(".result").html(data);
        console.log(data);

        gg1.refresh(getRandomInt(10, 35));
        gg2.refresh(data.temperatures[1].value);
        gg3.refresh(data.temperatures[2].value);
        gg4.refresh(data.temperatures[3].value);

        $('.rasp_temp').html(data.sysinfo.cpuTemp);
        $('.datetime').html(data.datetime);
        $('.rasp_diskusage').html(data.sysinfo.diskInfo[3]);
        $('.rasp_memusage').html(data.sysinfo.ramInfo[1]+' de '+data.sysinfo.ramInfo[0]);
    });
}

$(function () {
    getData();
});
setInterval(function () {
    getData();
}, 5000);
