<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'
import { Streamlit } from '~/stcomponentlib'
import { DsfrButtonGroup } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps.d.ts'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		align?: 'left' | 'center' | 'right'
		inlineLayoutWhen?: 'never' | 'always' | 'small' | 'medium' | 'large'
		reverse?: boolean
		iconRight?: boolean
		size?: 'small' | 'medium' | 'large'
		buttons?: {
			label?: string
			secondary?: boolean
			tertiary?: boolean
			disabled?: boolean
			icon?: string
			iconOnly?: boolean
			// iconRight?: boolean
			noOutline?: boolean
			// size?: '' | 'small' | 'sm' | 'lg' | 'large' | 'md' | 'medium'
			// Om
			// Custom props
			link?: string
			copy?: string
		}[]
		equisized?: boolean
	}>
>()

const clicked = ref<boolean>(false)
const isFocused = ref<boolean>(false)

const onRenderEvent = (_event: Event): void =>
	{
		if (!isFocused.value && clicked.value)
		{
			clicked.value = false
			Streamlit.setComponentValue(clicked.value)
		}
	}

onMounted(() =>
	{
		Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRenderEvent)
	})

onUnmounted(() =>
	{
		Streamlit.events.removeEventListener(Streamlit.RENDER_EVENT, onRenderEvent)
	})

const onClick = () =>
	{
		// TODO: Which button was clicked?
	}

const onFocus = () =>
	{
		isFocused.value = true
	}

const onBlur = () =>
	{
		isFocused.value = false
	}
</script>

<template>
	<div class="component" :style="style">
		<DsfrButtonGroup
			v-bind="props.args"
			:disabled="props.disabled || props.args.disabled"
			@click="onClick"
			@focus="onFocus"
			@blur="onBlur"
		/>
	</div>
</template>
