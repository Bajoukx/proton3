// MaxMSP statements

autowatch = 1;
inlets = 1;
outlets = 4;

var len = 512;
var real = new Buffer("real")
var imag = new Buffer("imag")
var mag = new Buffer("magnitude")

// This returns an empty wavefunction of length n.

function wavefunction(n) {
    var psi = [];
    for (var i = 0; i < n; i++) {
        psi[i] = { real: 0, imag: 0 }
    }
    return psi; // for example [{real:0, imag:0}, {real:0, imag:0}, ...]
}
// This takes the starting wavefunction, and returns the wavefunction a short time later.
function timestep(psi, dt) {

    dt = dt/0.002;

    // This is how many units of time we're going to try to step forward.
    psi = timestepV(psi, dt);
    psi = timestepT(psi, dt);
    return psi;
}

function timestepV(psi, dt) {
    // var n = psi.length;
    var n = len;
    for (var i = 0; i < n; i++) {
        // This is the x that is in the equation above.
        var x = (i - n / 2)
        // This is the potential at this point. >>>>>>>>>> POTENTIAL (OPEN CLOSED QUADRATIC FUNCTION)
        var V = x * x * 0.0015;
        var theta = dt * V;
        var c = Math.cos(theta);
        var s = Math.sin(theta);
        var re = psi[i].real * c - psi[i].imag * s;
        var im = psi[i].imag * c + psi[i].real * s;
        psi[i].real = re;
        psi[i].imag = im;
    }
    return psi;
}

function timestepT(psi, dt) {
    psi = FFT.fft(psi);
    // var n = psi.length;
    var n = len;
    for (var i = 1; i < n / 2; i++) {
        var k = 2 * 3.1415927 * i / n;
        var theta = k * k * dt;
        var c = Math.cos(-theta);
        var s = Math.sin(-theta);
        var re = psi[i].real * c - psi[i].imag * s;
        var im = psi[i].imag * c + psi[i].real * s;
        psi[i].real = re;
        psi[i].imag = im;


        var j = n - i;
        re = psi[j].real * c - psi[j].imag * s;
        im = psi[j].imag * c + psi[j].real * s;
        psi[j].real = re;
        psi[j].imag = im;

    }
    return FFT.fft(psi);
}

// This returns the initial state of the simulation .
var phase = len / 2;
// var mass = 1;
// var amplitude = 0.8;

function init(mass, amplitude) {
    var n = len;
    var psi = wavefunction(n);
    for (var i = 0; i < n; i++) {
        psi[i].real = Math.exp(-(i - phase) * (i - phase) / (mass * mass)) * amplitude;
        psi[i].imag = 0;
    }
    return psi;
}

function evaluate(dt, mass, amplitude) {

    // var samples = new Array;
    // var frames = buf.framecount();
    // var channels = buf.channelcount();
    psi = init(mass, amplitude);
    after = timestep(psi, dt);
    var n = len;
 
    for (var i = 0; i < n; i++) {
        mag.poke(1, i, getMag(after[i]));
        real.poke(1, i, after[i].real);
        imag.poke(1, i, after[i].imag);
    }

    real.send("setsize", n / 44);
    imag.send("setsize", n / 44);
    mag.send("setsize", n / 44);
    // post(n);
    // post(frames, channels);
}

function getMag(c) {
    return c.real * c.real + c.imag * c.imag; 
}



/*

    This version of fft.js is a translation of the wikipedia example for the cooley-tucker algorithm.

    Feel free to use this as you want, but the author does not accept liability.

    License: MIT.

    It only works with powers of two.

*/


var FFT = function () {
    var me = this;
    var b = [];
    var separate = function (a, S, E) {
        var n = E - S;
        for (var i = 0; i < n / 2; i++) {
            b[i] = a[S + i * 2 + 1];
        }

        //for(int i=0; i<n/2; i++)    // copy all odd elements to heap storage
        //b[i] = a[i*2+1];


        for (var i = 0; i < n / 2; i++)    // copy all even elements to lower-half of a[]
            a[S + i] = a[S + i * 2];
        for (var i = 0; i < n / 2; i++)    // copy all odd (from heap) to upper-half of a[]
            a[S + i + n / 2] = b[i];
    }

    var fft2 = function (X, S, E) {
        var N = E - S;
        if (N < 2) {
            // bottom of recursion.
            // Do nothing here, because already X[0] = x[0]
        } else {
            separate(X, S, E);      // all evens to lower half, all odds to upper half
            fft2(X, S, S + N / 2);   // recurse even items
            fft2(X, S + N / 2, E);   // recurse odd  items
            // combine results of two half recursions
            for (var k = 0; k < N / 2; k++) {
                var ereal = X[S + k].real;   // even
                var eimag = X[S + k].imag;   // even
                var oreal = X[S + k + N / 2].real;   // odd
                var oimag = X[S + k + N / 2].imag;   // odd
                // w is the "twiddle-factor"
                var theta = -2. * Math.PI * k / N;
                var wi = Math.sin(theta);
                var wr = Math.cos(theta);


                X[S + k].real = ereal + wr * oreal - wi * oimag;
                X[S + k].imag = eimag + wr * oimag + wi * oreal;
                X[S + k + N / 2].real = ereal - wr * oreal + wi * oimag;
                X[S + k + N / 2].imag = eimag - wr * oimag - wi * oreal;
            }
        }
    }
    me.fft = function (X) {
        var a = [];
        for (var i = 0; i < X.length; i++) {
            a[i] = {
                real: X[i].real,
                imag: X[i].imag
            };
        }
        fft2(a, 0, a.length);
        var l = 1.0 / Math.sqrt(a.length);
        for (var i = 0; i < a.length; i++) {
            a[i].imag = -a[i].imag * l;
            a[i].real = a[i].real * l;
        }
        return a;
    }

    var transpose = function (X) {
        var ret = [];
        for (var i = 0; i < X[0].length; i++) {
            ret[i] = [];
            for (var j = 0; j < X.length; j++) {
                ret[i][j] = X[j][i];
            }
        }
        return ret;
    }

    me.fft2d = function (X) {
        var ret = [];
        for (var i = 0; i < X.length; i++) {
            ret[i] = me.fft(X[i]);
        }
        ret = transpose(ret);
        for (var i = 0; i < X.length; i++) {
            ret[i] = me.fft(ret[i]);
        }
        return transpose(ret);
    }
}

var FFT = new FFT();
