For this exe to work propperly the following is needed:

You have to install SQL server management studio
You have to create a new Database with the following atributes:
	*Database name: Barcodes
	*new Table: Filtered_Barcodes
	*Table fields: INDEX and Barcode
	*Field specs: -INDEX should be primary key
		      -INDEX type should be type "int"
		      -INDEX double click on (is Identity)
		      -Barcode should be of type "VARCHAR(MAX)"
		**No nulls are allowed for both fields***
