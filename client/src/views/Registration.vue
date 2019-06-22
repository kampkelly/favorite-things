<template>
    <div>
        <div class="registration-container">
            <div class="registration-bar">
                <div>
                    <router-link to="/registration/signup">Signup</router-link>
                </div>
                <div>
                    <router-link to="/registration/signin">Signin</router-link>
                </div>
            </div>
            <router-view></router-view>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.registration-container {
    width: 60%;
    margin: auto;
    .registration-bar {
        display: flex;
        padding: 10px;
        margin-bottom: 50px;
        > div:nth-child(1) {
            background: #6202EE;
            padding: 10px;
            flex: 1;
            margin-right: 10px;
            a {
                color: white;
            }
        }
        > div:nth-child(2) {
            background: #6202EE;
            padding: 10px;
            flex: 1;
            a {
                color: white;
            }
        }
    }
}
</style>
