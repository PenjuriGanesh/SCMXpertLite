document.getElementById('shipment-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Perform additional validation
    const sinum = document.getElementById('sinum').value;
    const cnum = document.getElementById('cnum').value;
    const goodsno = document.getElementById('goodsno').value;
    const rdetails = document.getElementById('rdetails').value;
    const gdtypes = document.getElementById('gdtypes').value;
    const device = document.getElementById('device').value;
    const exdate = document.getElementById('exdate').value;
    const ponum = document.getElementById('ponum').value;
    const delnum = document.getElementById('delnum').value;
    const ndcnum = document.getElementById('ndcnum').value;
    const bid = document.getElementById('bid').value;
    const sdesc = document.getElementById('sdesc').value;

    // Basic validation checks
    if (!sinum || !cnum || !goodsno || !rdetails || !gdtypes || !device || !exdate || !ponum || !delnum || !ndcnum || !bid || !sdesc) {
        alert('All fields are required.');
        return;
    }

    // If all validations pass
    alert('Shipment details submitted successfully!');

    // Reset the form after successful submission
    document.getElementById('shipment-form').reset();
});

// Optionally clear inputs on cancel
function clearinput() {
    document.querySelector("form").reset();
}
