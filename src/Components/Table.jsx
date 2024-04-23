import React, { useEffect, useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import axios from 'axios';
import { CircularProgress, Box, Card, CardContent, Typography } from '@mui/material';

const columns = [
    { field: 'id', headerName: 'ID', width: 90 },
    { field: 'make', headerName: 'Make', width: 150 },
    { field: 'model', headerName: 'Model', width: 150 },
    { field: 'year', headerName: 'Year', width: 110 },
    { field: 'engine_type', headerName: 'Engine Type', width: 160 },
    { field: 'horsepower', headerName: 'Horsepower', type: 'number', width: 130 },
    { field: 'fuel_efficiency', headerName: 'Fuel Efficiency', width: 180 },
    { field: 'safety_rating', headerName: 'Safety Rating', type: 'number', width: 140 },
    { field: 'interior', headerName: 'Interior', width: 130 },
    { field: 'color', headerName: 'Color', width: 130 },
    { field: 'price', headerName: 'Price', type: 'number', width: 130 }
];

const DataTable = () => {
    const [allData, setAllData] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const pageSize = 5;

    const fetchData = async () => {
        setLoading(true);
        try {
            await new Promise(resolve => setTimeout(resolve, 2000));
            const response = await axios.get('http://localhost:3000/cars');
            setAllData(response.data);
            setLoading(false);
        } catch (error) {
            setError(error);
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchData();
    }, []);


    if (loading) return (
        <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
            <CircularProgress />
        </Box>
    );

    if (error) return (
        <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
            <Card>
                <CardContent>
                    <Typography color="error">Error: {error.message}</Typography>
                </CardContent>
            </Card>
        </Box>
    );

    return (
        <div>
            <Box sx={{ height: 700, width: '100%' }}>
                <DataGrid
                    rows={allData}
                    columns={columns}
                    initialState={{
                        pagination: {
                            paginationModel: {
                                pageSize: pageSize,
                            },
                        },
                    }}
                    pageSizeOptions={[5]}
                    checkboxSelection
                    disableRowSelectionOnClick
                />
            </Box>
        </div>
    );
}

export default DataTable;
