<template>
    <div>
        <div class="registration-container">
            <h4 class="registration-title">Welcome, keep a list of the things that matter to you!</h4>
            <div class="registration-bar">
                <router-link to="/registration/signup">Signup</router-link>
                <router-link to="/registration/signin">Signin</router-link>
            </div>
            <router-view></router-view>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.registration-container {
    width: 60%;
    margin: auto;
    .registration-title {
        color: gray;
    }
    .registration-bar {
        display: flex;
        padding: 10px 0px 10px 0px;
        margin-bottom: 40px;
        a {
            background: #6202EE;
            padding: 10px;
            flex: 1;
            color: white;
            &:hover {
                color: #cfcfcf;
            }
        }
        > a:nth-child(1) {
            margin-right: 10px;
        }
    }
}
</style>
