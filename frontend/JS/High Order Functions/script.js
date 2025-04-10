function FilterArray(){
    let l = [0,1,2,3,4,5,6,7,8,9];

    const Arrow = l.filter( i => i%2==0 );

    console.log(Arrow);


    const Arrow2 = l.filter( (i) =>{
        return i%2==0;
    });


    console.log(Arrow2);


    const AnFunc = l.filter(function(i){
        return i%2==0;
    })

    console.log(AnFunc);


    function even(i){
        return i%2==0
    }

    const func = l.filter(even);


    console.log(func);

}


function MapArray(){
    let l = [0,1,2,3,4,5,6,7,8,9];

    const Arrow = l.map( i=> i*2 );
    console.log(Arrow);

    const Arrow2 = l.map( (i)=>{
        return i*2;
    });
    console.log(Arrow2);

    const AnFunc = l.map( function(i){
        return i*2;
    });
    console.log(AnFunc);

    function doubleN(i){
        return i*2;
    }

    const func = l.map(doubleN);
    console.log(func);

}



function ReduceArray(){
    let l = [0,1,2,3,4,5,6,7,8,9];

    const Arrow = l.reduce( (a,b)=> a+b );
    console.log(Arrow);

    const Arrow2 = l.reduce( (a,b)=>{
        return a+b;
    });
    console.log(Arrow2);

    const AnFunc = l.reduce( function(a,b){
        return a+b;
    });
    console.log(AnFunc);

    function doubleN(a,b){
        return a+b;
    }

    const func = l.reduce(doubleN);
    console.log(func);

}