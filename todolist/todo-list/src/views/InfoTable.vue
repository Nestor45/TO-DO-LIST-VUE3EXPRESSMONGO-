<template>
    <v-container>
        <v-card elevation="2" outlined tile>
            <v-card-text>
                <p class="text-h4 text--primary text-center">
                    eleemosynary
                </p>
                <v-layout class="justify-end">
                    <v-btn
                        color="primary"
                        class="mb-2 "
                        @click="newItem()"
                    >
                        New Item
                    </v-btn>
                </v-layout>
            </v-card-text>
            <v-dialog v-model="dialog" max-width="600px">
                <v-card>
                    <v-card-title>
                        <span class="text-h5" >{{ formTitle }}</span>
                    </v-card-title>
                    <v-card-text>
                        <v-container>
                             <v-form ref="form" v-model="valid" >
                                <v-row>
                                    <v-col cols="12">
                                        <v-text-field
                                        v-model="editedItem.name"
                                        :rules="nameRules"
                                        label="Task name*"
                                        required
                                        ></v-text-field>
                                    </v-col>
                                    <v-col cols="12">
                                        <v-text-field
                                        v-model="editedItem.description"
                                        :rules="descriptionRules"
                                        label="Comment task*"
                                        required
                                        ></v-text-field>
                                    </v-col>
                                    <v-col cols="12">
                                        <v-text-field
                                        v-model="editedItem.comment"
                                        :rules="commentRules"
                                        label="Description task*"
                                        hint="example:"
                                        persistent-hint
                                        required
                                        ></v-text-field>
                                    </v-col>
                                    <v-col
                                        cols="12"
                                        sm="6"
                                    >
                                        <v-select
                                        v-model="editedItem.status"
                                        :rules="statusRules"
                                        :items="['Pending', 'Cancel', 'Finished']"
                                        label="Status*"
                                        required
                                        ></v-select>    
                                    </v-col>
                                </v-row>
                            </v-form>
                        </v-container>
                        <small>*indicates required field</small>
                    </v-card-text>
                    <v-card-actions>
                    <v-spacer></v-spacer>
                        <v-btn
                            color="blue darken-1"
                            text
                            @click="dialog = false"
                        >
                            Close
                        </v-btn>
                        <v-btn
                            color="blue darken-1"
                            text
                            :disabled="!valid"
                            @click="save"
                        >
                            Save
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
            <v-table>
                <thead>
                    <tr>
                        <th class="text-left">
                        Name
                        </th>
                        <th class="text-left">
                        Description
                        </th>
                        <th class="text-left">
                        Comment
                        </th>
                        <th class="text-left">
                        Status
                        </th>
                        <th class="text-left">
                        Actions
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                        v-for="(task, i) in tasks"
                        :key="i"
                    >
                        <td>{{ task.name }}</td>
                        <td>{{ task.description }}</td>
                        <td>{{ task.comment }}</td>
                        <td>{{ task.status }}</td>
                        <v-btn icon="mdi-file-document-edit" class="ma-2" variant="text" @click="editItem(task)"></v-btn>
                        <v-btn icon="mdi-delete-forever" class="ma-2" variant="text" @click="deleteItem(task)"></v-btn>
                    </tr>
                </tbody>
            </v-table>
            
        </v-card>
    </v-container>
</template>

<script setup>
    import { ref, computed, watchEffect } from 'vue'
    import { axios } from 'axios'

    const dialog = ref(false)
    let editedIndex = ref(-1)
    let valid = ref(true)
    const form = ref(null)

    let editedItem = ref ({
        name: '',
        description: '',
        comment: '',
        status: '',
    })

    let defaultItem = ref ({
        name: '',
        description: '',
        comment: '',
        status: '',
    })

    const tasks = ref([])

    const nameRules= ref ([
        v => !!v || 'Task is required',
    ])
    const descriptionRules= ref ([
        v => !!v || 'Description is required',
    ])
    const commentRules= ref ([
        v => !!v || 'Comment is required',
    ])
    const statusRules= ref ([
        v => !!v || 'Status is required',
    ])

    const formTitle = computed(() =>
        editedIndex.value === -1 ? 'New Item' : 'EDIT ALL FIELDS*'
    )
    
    watchEffect ( async() => {
        try {
            const response  = await fetch('http://127.0.0.1:4000/api/tasks')
            tasks.value = await response.json()
        } catch (error) {
            console.log(error)
        }
    })

    const newItem = () => {
        editedIndex.value = -1
        editedItem.value = Object.assign({}, defaultItem.value)
        dialog.value = true
    }

    const save = async() => {
        try {
            if (editedIndex.value >= 0) {
                console.log("valid:",valid.value)
                console.log("editedItem",editedItem.value._id)
                await fetch(`http://127.0.0.1:4000/api/tasks/${editedItem.value._id}`, {
                method: 'PUT', // or 'PUT'
                body: JSON.stringify(editedItem.value), // data can be `string` or {object}!
                headers:{
                    'Content-Type': 'application/json'
                }
            }).then(res => res.json())
                .catch(error => {console.error('Error:', error)})
                .then(response => {
                    console.log('Success:', response),
                    Object.assign(tasks.value[editedIndex.value], editedItem.value)
                })
            } else {
                
                await fetch('http://127.0.0.1:4000/api/tasks', {
                    method: 'POST', // or 'PUT'
                    body: JSON.stringify(editedItem.value), // data can be `string` or {object}!
                    headers:{
                        'Content-Type': 'application/json'
                    }
                }).then(res => res.json())
                    .catch(error => {console.error('Error:', error)})
                    .then(response => {
                        console.log('Success:', response), 
                        tasks.value.push(response)
                    })
            }
            dialog.value = false
        } catch (error) {
            console.log(error)
        }
    }
    
    const editItem = (item) => {
        dialog.value = true
        editedIndex.value = tasks.value.indexOf(item)
        editedItem.value = Object.assign({}, item)
    }

    const deleteItem = async (item) => {
        console.log(item._id)
        editedIndex.value = tasks.value.indexOf(item)
        editedItem.value = Object.assign({}, item)
        try {
            await fetch(`http://127.0.0.1:4000/api/tasks/${item._id}`, {
                method: 'DELETE', // or 'PUT'
                headers:{
                    'Content-Type': 'application/json'
                }
            }).then(res => res.json())
                .catch(error => {console.error('Error:', error)})
                .then(response => {
                    console.log('Success:', response),
                       tasks.value.splice(editedIndex.value, 1)
                })
            dialog.value = false
        } catch (error) {
            console.log(error)
        }
    }
</script>